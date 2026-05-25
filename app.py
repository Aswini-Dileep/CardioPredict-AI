from flask import Flask, render_template, request
import pandas as pd
import pickle
import shap
#from mistralai import Mistral
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

app = Flask(__name__)

load_dotenv()

# Load trained model
model = pickle.load(open("heart_disease_model.pkl", "rb"))

# Mistral API Configuration

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

client = MistralClient(api_key=MISTRAL_API_KEY)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        required_fields = [
            "age", "sex", "cp", "bp", "chol",
            "fbs", "ekg", "max_hr", "ex_angina",
            "st_dep", "slope", "vessels", "thal"
        ]

        for field in required_fields:

            if request.form.get(field) == "" or request.form.get(field) is None:

                return render_template(
                    "index.html",
                    error="⚠️ Please fill all fields before prediction."
                )

        age = float(request.form["age"])

        sex = 1 if request.form["sex"] == "Male" else 0

        cp = int(request.form["cp"])

        bp = float(request.form["bp"])

        chol = float(request.form["chol"])

        fbs = 1 if request.form["fbs"] == "Yes" else 0

        ekg = int(request.form["ekg"])

        max_hr = float(request.form["max_hr"])

        ex_angina = 1 if request.form["ex_angina"] == "Yes" else 0

        st_dep = float(request.form["st_dep"])

        slope = int(request.form["slope"])

        vessels = int(request.form["vessels"])

        thal = int(request.form["thal"])


        input_data = pd.DataFrame({

            "Age":[age],

            "Sex":[sex],

            "Chest pain type":[cp],

            "BP":[bp],

            "Cholesterol":[chol],

            "FBS over 120":[fbs],

            "EKG results":[ekg],

            "Max HR":[max_hr],

            "Exercise angina":[ex_angina],

            "ST depression":[st_dep],

            "Slope of ST":[slope],

            "Number of vessels fluro":[vessels],

            "Thallium":[thal]

        })

        prediction = model.predict(input_data)[0]

        prob = model.predict_proba(input_data)[0][1]


        # ---------------- SHAP Explainability ----------------

        explainer = shap.Explainer(model)

        shap_values = explainer(input_data)

        plt.clf()

        plt.figure(figsize=(10,5))

        shap.plots.waterfall(shap_values[0], show=False)

        plt.savefig(
            "static/shap_plot.png",
            bbox_inches="tight",
            dpi=300
        )

        plt.close()


        risk_percent = round(prob * 100, 2)

        if prediction == 1:

            result = "High Risk of Heart Disease"

            result_class = "high-risk"

            bar_color = "#ef4444"

        else:

            result = "Low Risk of Heart Disease"

            result_class = "low-risk"

            bar_color = "#22c55e"


        # ---------------- INTERPRETATION ----------------

        if prob > 0.7:

            interpretation = "🔴 High Risk: Immediate medical consultation recommended."

            recommendations = [
                "Consult a cardiologist immediately",
                "Undergo further diagnostic tests",
                "Monitor blood pressure regularly"
            ]

        elif prob > 0.4:

            interpretation = "🟠 Moderate Risk: Lifestyle changes and routine checkups recommended."

            recommendations = [
                "Exercise regularly",
                "Maintain healthy diet",
                "Reduce stress and improve sleep"
            ]

        else:

            interpretation = "🟢 Low Risk: Maintain healthy lifestyle habits."

            recommendations = [
                "Continue regular exercise",
                "Maintain balanced diet",
                "Routine health monitoring"
            ]

    
        return render_template(
            "index.html",
            prediction_text=result,
            result_class=result_class,
            risk_percent=risk_percent,
            bar_color=bar_color,
            interpretation=interpretation,
            recommendations=recommendations
        )
    

    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    try:

        user_message = request.form["message"]

        response = client.chat(

            model="mistral-small-latest",

            messages=[

                ChatMessage(
                    role="system",
                    content=(
                        "You are a professional AI healthcare assistant. "
                        "Give simple, educational, and safe answers "
                        "about heart health."
                    )
                ),

                ChatMessage(
                    role="user",
                    content=user_message
                )

            ]
        )

        reply = response.choices[0].message.content

        return {
            "reply": reply
        }

    except Exception as e:

        return {
            "reply": f"Error: {str(e)}"
        }
    
    
if __name__ == "__main__":
    app.run(debug=True)