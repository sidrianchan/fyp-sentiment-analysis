# Sentiment Analysis – Final-Year Project  
![CI](https://github.com/sidrianchan/fyp-sentiment-analysis/actions/workflows/ci.yml/badge.svg)

A lightweight BERT-based sentiment classifier for the Amazon Fine-Food Reviews
dataset.  Artefacts frozen for COM3001 assessment (tag **v1.0-snapshot**).

## Licensing
- **Code and Documentation**: Licensed under the [MIT License](LICENSE).
- **Amazon Fine-Food Reviews Dataset**: Available from [Kaggle](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) under its respective terms.
- **Pre-trained Weights**: The fine-tuned BERT weights (`artefacts/weights/bert_base_finetuned.zip`) are distributed under the MIT License, but the base BERT model is subject to the [Apache 2.0 License](https://github.com/google-research/bert/blob/master/LICENSE).
- **Dependencies**: This project uses third-party libraries listed in `requirements.txt`. Refer to each library’s repository for its license (e.g., Apache 2.0 for Hugging Face Transformers, MIT for PyTorch).


## Dataset Setup
**Download the Dataset**:
   - Download `Reviews.csv` from [Kaggle: Amazon Fine-Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews).
   - Place the file in the `data/raw/` directory: `mkdir data && mv Reviews.csv data/raw`.

---

## Quick-start

```bash
# Clone & enter repo
git clone https://github.com/sidrianchan/fyp-sentiment-analysis.git
cd fyp-sentiment-analysis

# Make a Python 3.10 virtual-env  (brew install python@3.10 if needed)
python3.10 -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download & unzip weight (170 MB)
mkdir -p artefacts/weights
curl -L -o artefacts/weights/bert.zip \
  https://github.com/sidrianchan/fyp-sentiment-analysis/releases/download/v1.0-snapshot/bert_base_finetuned.zip
unzip -q artefacts/weights/bert.zip -d artefacts/weights && rm artefacts/weights/bert.zip

# Run smoke-test + demo
pytest -q
python - <<'PY'
from src.infer import predict
print(predict(["Great taste!", "Terrible service."]))
PY
