# t-c-risk-detector

A machine learning-based tool for automated legal risk detection in Terms & Conditions (T&C) and legal documents. This repository provides a pretrained transformer model (Legal-BERT) fine-tuned for legal risk classification, along with all necessary configs and tokenizers for easy deployment and inference.

---

## Features

- **Legal Risk Detection**: Predicts risk categories in legal text (T&C, contracts, privacy policies, etc.)
- **Pretrained Model**: Based on [nlpaueb/legal-bert-base-uncased](https://huggingface.co/nlpaueb/legal-bert-base-uncased) for superior performance on legal language.
- **Easy Integration**: All model, tokenizer, and config files included for quick use in Python ML/NLP pipelines.
- **Extensible**: Can be further fine-tuned on custom legal datasets.
- **Multi-class Classification**: Supports multiple risk categories (see config for details).

---

## Repository Structure

```
t-c-risk-detector/
└── Legal Risk Model/
    ├── config.json                # Model architecture & label mapping
    ├── model.safetensors          # Pretrained & fine-tuned model weights
    ├── special_tokens_map.json    # Special token mapping for tokenizer
    ├── tokenizer.json             # Full tokenizer configuration
    ├── tokenizer_config.json      # Tokenizer settings
    └── vocab.txt                  # Vocabulary file
```

---

## Usage

### 1. Load Model & Tokenizer (HuggingFace Transformers, PyTorch)
```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

model_path = "path/to/Legal Risk Model"
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)

text = "Your terms and conditions text goes here."
inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
outputs = model(**inputs)
pred = torch.argmax(outputs.logits, dim=1).item()
print("Predicted risk label:", pred)
```

### 2. Prediction Labels

See `config.json` for mapping. Example:
```json
"id2label": {
  "0": "LABEL_0",
  "1": "LABEL_1",
  "2": "LABEL_2"
}
```
Customize `LABEL_0`, `LABEL_1`, etc. as per your dataset/classes.

### 3. Fine-tuning / Extension

You can further fine-tune the model with HuggingFace Trainer or your own pipeline by using the `model.safetensors` and tokenizer files.

---

## Requirements

- Python 3.8+
- `transformers` (v4.48.3 or compatible)
- `torch`
- (Optional) `safetensors`

Install with:
```bash
pip install transformers torch safetensors
```

---

## Pretrained Model

The pretrained and fine-tuned model is available on Hugging Face:
- **[sivanimohan/legal-risk-model](https://huggingface.co/sivanimohan/legal-risk-model)**

You can load the model directly from Hugging Face like this:
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("sivanimohan/legal-risk-model")
model = AutoModelForSequenceClassification.from_pretrained("sivanimohan/legal-risk-model")
```

---

## References

- [Legal-BERT Model](https://huggingface.co/nlpaueb/legal-bert-base-uncased)
- [HuggingFace Model Card: sivanimohan/legal-risk-model](https://huggingface.co/sivanimohan/legal-risk-model)
- [HuggingFace Transformers Documentation](https://huggingface.co/docs/transformers/index)

---

## License

MIT License

---

**Automate legal risk analysis in your workflow with t-c-risk-detector!**
