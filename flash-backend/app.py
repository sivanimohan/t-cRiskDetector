from flask import Flask, request, jsonify
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np

app = Flask(__name__)

# Load your model
model_path = "sivanimohan/legal-risk-model"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def predict_risk(text):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    probs = torch.nn.functional.softmax(logits, dim=1).cpu().numpy()
    risk_level = np.argmax(probs, axis=1)[0]
    confidence = probs[0][risk_level]
    return risk_level, confidence

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get("text")
    if text:
        risk_level, confidence = predict_risk(text)
        risk_label = ["Low Risk", "Medium Risk", "High Risk"][risk_level]
        return jsonify({"risk": risk_label, "confidence": confidence * 100})
    return jsonify({"error": "No text provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
