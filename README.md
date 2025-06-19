Terms and Conditions Risk Detector

📌 Overview

The Terms and Conditions Risk Detector is a machine learning-based tool that analyzes legal documents, particularly terms and conditions, to assess their risk levels. This model helps users identify clauses that may have potential legal implications, ensuring better awareness before agreeing to terms.
Google Colab Notebook : https://colab.research.google.com/drive/1GwIF-Nxpy7Jd9e6Zv-opGE6x-UBlxlXQ#scrollTo=PWj3a8GFL8zy

🚀 Features

AI-Powered Risk Assessment: Categorizes terms into low, medium, or high-risk levels.

Natural Language Processing (NLP): Utilizes a fine-tuned transformer model to understand legal text.

Confidence Scoring: Provides probability scores for each risk category.

CSV-Based Analysis: Allows bulk processing of legal documents.

📂 Dataset

The model was trained using a dataset of various terms and conditions extracted from online agreements, labeled with risk levels by legal experts.

📖 How It Works

Preprocess Text: The input document is tokenized and prepared for analysis.

Model Prediction: The trained AI model predicts the risk level.

Output Interpretation: The model assigns a risk category and confidence scores to each clause.

🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/sivanimohan/t-cRiskDetector.git
cd t-cRiskDetector

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Model

python predict.py --text "By using our services, you consent to data sharing with third parties."

📊 Example Output

Predicted Risk Level: High
Confidence Scores: [0.02, 0.05, 0.93]

🔧 Model Training & Fine-Tuning

To train the model on new data:

python train.py --dataset legal_risk_analysis.csv

📜 License

This project is open-source and available under the MIT License.

👩‍💻 Author

Developed by Sivani Mohan

GitHub: sivanimohan

LinkedIn: Sivani Mohan

⭐ Contribute

Pull requests are welcome! Feel free to open an issue for suggestions or improvements.

