from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load pre-trained model (or your fine-tuned model)
model = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get("text")
    if text:
        result = model(text)[0]
        return jsonify({"risk": result['label'], "confidence": result['score'] * 100})
    return jsonify({"error": "No text provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
