# Sentiment Analysis – Final-Year Project  
![CI](https://github.com/sidrianchan/fyp-sentiment-analysis/actions/workflows/ci.yml/badge.svg)

A lightweight BERT-based sentiment classifier for the Amazon Fine-Food Reviews
dataset.  Artefacts frozen for COM3001 assessment (tag **v1.0-snapshot**).

---

## Quick-start (CPU, no training)

```bash
git clone https://github.com/sidrianchan/fyp-sentiment-analysis.git
cd fyp-sentiment-analysis
pip install -r requirements.txt              # PyTorch + Transformers etc.
pytest -q                                    # 6-second smoke-test
python - <<'PY'
from src.infer import predict
print(predict(["Great taste!", "Terrible service."]))
PY
