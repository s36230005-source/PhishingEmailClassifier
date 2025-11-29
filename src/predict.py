import joblib
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "random_forest_tfidf_model.pkl")
model = joblib.load(model_path)

def predict_email(text):
    """
    Returns label and probability
    """
    prob = model.predict_proba([text])[0]
    pred = model.predict([text])[0]

    label = "Phishing" if pred == 1 else "Legitimate"
    confidence = max(prob)

    return label, confidence
