# Sentiment Analysis – Final-Year Project  
![CI](https://github.com/sidrianchan/fyp-sentiment-analysis/actions/workflows/ci.yml/badge.svg)

A lightweight BERT-based sentiment classifier for the Amazon Fine-Food Reviews
dataset.  Artefacts frozen for COM3001 assessment (tag **v1.0-snapshot**).

---

## Quick-start (CPU, no training)

```bash
# Clone + install Python deps
git clone https://github.com/sidrianchan/fyp-sentiment-analysis.git
cd fyp-sentiment-analysis
pip install -r requirements.txt

# Download the pre-trained weight (~170 MB) and unzip
mkdir -p artefacts/weights
curl -L -o artefacts/weights/bert.zip \
  https://github.com/sidrianchan/fyp-sentiment-analysis/releases/download/v1.0-snapshot/bert_base_finetuned.zip
unzip -q artefacts/weights/bert.zip -d artefacts/weights
rm artefacts/weights/bert.zip

# Run the smoke-test and a demo prediction
pytest -q
python - <<'PY'
from src.infer import predict
print(predict(["Great taste!", "Terrible service."]))
PY
