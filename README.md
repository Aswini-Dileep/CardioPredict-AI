# 🧑‍⚕️ CardioPredict AI

AI-Powered Heart Disease Risk Prediction System built using Machine Learning, Flask, SHAP Explainability, and Mistral AI.

---

## 🚀 Live Demo

🌍 **Live App:**  
https://cardiopredict-ai-0jet.onrender.com

📂 **GitHub Repository:**  
https://github.com/Aswini-Dileep/CardioPredict-AI

---

# 📌 Project Overview

CardioPredict AI is an intelligent healthcare web application designed to predict the risk of heart disease using clinical patient data.

The system combines:

- Machine Learning prediction
- SHAP Explainability
- AI-powered healthcare chatbot
- Modern responsive Flask UI
- Cloud deployment using Render

This application helps users understand their cardiac risk factors through interactive prediction analysis and AI-assisted healthcare guidance.

---

# 🎯 Objective

The main objective of this project is to:

- Build a machine learning model to predict heart disease risk
- Develop a user-friendly healthcare web application
- Provide meaningful interpretation of predictions
- Implement explainable AI for transparency
- Simulate a clinical decision support system

---

# 🏥 Real-World Use Case

This system can be used in:

- Hospital OPD (Outpatient Department)
- Telemedicine platforms
- Health screening camps
- Preventive healthcare systems

### Example Scenario

A healthcare worker inputs patient details →  
The system predicts heart disease risk →  
High-risk patients are prioritized for doctor consultation.

---

# 📊 Dataset Description

The dataset contains approximately **630,000 records** with clinical healthcare features including:

- Age
- Sex
- Chest Pain Type
- Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- EKG Results
- Maximum Heart Rate
- Exercise Angina
- ST Depression
- Slope of ST
- Number of Vessels
- Thallium Test
- Heart Disease (Target)

The dataset includes both categorical and numerical features.

---

# ⚙️ Project Workflow

## 1️⃣ Data Understanding

- Explored dataset structure and feature meanings
- Identified categorical and numerical variables
- Understood medical significance of features

---

## 2️⃣ Exploratory Data Analysis (EDA)

Performed:

- Statistical summary analysis
- Distribution plots
- Correlation heatmaps
- Feature relationship analysis
- Medical risk pattern analysis

---

## 3️⃣ Data Preprocessing

- Encoded categorical variables
- Handled feature formatting
- Verified missing values
- Prepared model-ready dataset

---

## 4️⃣ Feature Importance Analysis

Used tree-based methods to identify important medical features.

### Top Contributing Features

- Thallium Test
- Chest Pain Type
- ST Depression
- Maximum Heart Rate
- Number of Vessels

---

## 5️⃣ Model Building

Trained multiple machine learning models:

- Logistic Regression
- Random Forest
- Decision Tree
- XGBoost

---

## 6️⃣ Model Evaluation

Evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score

| Model               | Accuracy | Precision | Recall | F1 Score |
|--------------------|----------|-----------|--------|----------|
| Logistic Regression | ~0.88 | ~0.87 | ~0.85 | ~0.86 |
| Random Forest | ~0.88 | ~0.87 | ~0.86 | ~0.86 |
| **XGBoost** | **~0.89** | **~0.88** | **~0.86** | **~0.87** |
| Decision Tree | ~0.82 | ~0.80 | ~0.80 | ~0.80 |

✅ **XGBoost was selected as the final model**

---

## 7️⃣ Cross Validation

- Applied 5-fold cross validation
- Achieved stable model performance
- Mean F1-score: ~0.87

This confirms the model generalizes well.

---

# 🧠 Final Model

### Algorithm Used
- XGBoost Classifier

### Output
- Heart disease prediction
- Risk probability score
- Clinical interpretation
- Personalized recommendations

---

# 💻 Web Application

The application was built using Flask and deployed on Render.

---

## ✨ Features

### ✅ Heart Disease Prediction
- Real-time prediction system
- Risk probability analysis
- Interactive patient input form

### ✅ SHAP Explainability
- Explains why predictions were made
- Feature contribution visualization
- Improves AI transparency

### ✅ AI Healthcare Assistant
- Integrated Mistral AI chatbot
- Real-time healthcare Q&A
- Educational heart-health support

### ✅ Clinical Interpretation
- Risk categorization
- Personalized recommendations
- Lifestyle guidance

### ✅ Modern Responsive UI
- Glassmorphism healthcare design
- Mobile responsive layout
- Professional medical interface

---

# 📈 SHAP Explainability

The project integrates SHAP (SHapley Additive exPlanations) to improve model transparency.

Users can understand:

- Which medical factors increased risk
- Which factors reduced risk
- Why the AI made a prediction

This improves trust and interpretability of machine learning predictions.

---

# 📸 Project Screenshots

## 🏠 Home Page
(Add Screenshot Here)

---

## 📊 Prediction Result
(Add Screenshot Here)

---

## 🧠 SHAP Explainability
(Add Screenshot Here)

---

## 🤖 AI Healthcare Assistant
(Add Screenshot Here)

---

# 🩺 Clinical Interpretation Logic

The prediction probability is categorized as:

- 🔴 High Risk (Probability > 0.7)
- 🟠 Moderate Risk (0.4 – 0.7)
- 🟢 Low Risk (< 0.4)

This improves usability in real healthcare scenarios.

---

# 💡 Recommendation System

Recommendations are dynamically generated based on:

- Prediction result
- Risk probability
- Clinical input values

### Example Recommendations

### High Risk
- Immediate cardiologist consultation
- Diagnostic testing
- Blood pressure monitoring

### Moderate Risk
- Lifestyle improvements
- Exercise recommendations
- Routine health checkups

### Low Risk
- Maintain healthy habits
- Continue regular exercise
- Balanced diet

---

# 🚧 Challenges Faced

- Understanding encoded medical features
- Managing Flask deployment issues
- Dependency conflicts during cloud deployment
- Implementing SHAP explainability
- Integrating Mistral AI chatbot
- Creating production-ready UI

---

# 📚 Key Learnings

- End-to-end ML deployment
- Flask web development
- Explainable AI using SHAP
- API integration
- Cloud deployment using Render
- Production dependency management
- UI/UX design for healthcare systems

---

# 🚀 Deployment

- Deployed using Render
- Production deployment with Gunicorn
- GitHub-integrated deployment workflow

🌍 Live Deployment:
https://cardiopredict-ai-0jet.onrender.com

---

# 🛠️ Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- Flask
- Python

## Machine Learning
- Scikit-learn
- XGBoost
- SHAP

## AI Integration
- Mistral AI API

## Deployment
- Render
- Gunicorn
- GitHub

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Aswini-Dileep/CardioPredict-AI.git
```

## Navigate to Project Folder

```bash
cd CardioPredict-AI
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Flask App

```bash
python app.py
```

---


## 📁 Project Structure

```text
CardioPredict-AI/
│
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── render.yaml
├── .env
│
├── static/
│   ├── bg.png
│   └── shap_plot.png
│
├── templates/
│   └── index.html
│
└── heart_disease_model.pkl
```

---

## ⚠️ Disclaimer

This application is designed for educational and informational purposes only.

It should NOT be considered a substitute for professional medical diagnosis or healthcare advice.

Always consult a qualified healthcare professional.

---

## ⭐ Future Improvements

* User authentication
* Patient history tracking
* PDF report generation
* Doctor dashboard
* Advanced AI recommendations
* Multi-disease prediction system

---

🏁 Conclusion

CardioPredict AI demonstrates a complete end-to-end machine learning pipeline from data analysis to real-world deployment.

The project successfully combines:

Machine Learning
Explainable AI
Healthcare analytics
AI chatbot integration
Modern web development
Cloud deployment

This system highlights how AI can support early disease detection and healthcare decision support systems.

---

## 👨‍💻 Author

### Aswini Dileep

* GitHub: [https://github.com/Aswini-Dileep](https://github.com/Aswini-Dileep)
* LinkedIn: www.linkedin.com/in/aswini-dileep

---

## 💙 Built With Passion for AI & Healthcare
