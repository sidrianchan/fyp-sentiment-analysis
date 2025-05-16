# Sentiment Analysis – Final-Year Project  
![CI](https://github.com/sidrianchan/fyp-sentiment-analysis/actions/workflows/ci.yml/badge.svg)

This repo contains the notebooks, helper code and **pre-trained BERT weights** used in my COM3001 project report (tag **v1.0-snapshot**).

## Quick-start (CPU, no training)

```bash
git clone https://github.com/sidrianchan/fyp-sentiment-analysis.git
cd fyp-sentiment-analysis
pip install -r requirements.txt
pytest -q                  # smoke-test <6 s
python - <<'PY'
from src.infer import predict
print(predict(["Great taste!", "Terrible service."]))
PY
