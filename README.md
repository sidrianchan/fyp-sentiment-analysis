# Sentiment Analysis – Final-Year Project  
![CI](https://github.com/sidrianchan/fyp-sentiment-analysis/actions/workflows/ci.yml/badge.svg)

A lightweight BERT-based sentiment classifier for the Amazon Fine-Food Reviews
dataset.  Artefacts frozen for COM3001 assessment (tag **v1.0-snapshot**).

---

## Quick-start (CPU, no training)

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
