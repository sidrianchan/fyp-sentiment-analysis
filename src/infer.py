# src/infer.py
"""
Lightweight inference wrapper for the pre-trained BERT sentiment model.
No training here – just load weights and predict on a list of texts.
"""

import pathlib
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Path to the weight file inside artefacts/weights/
WEIGHTS = (
    pathlib.Path(__file__).resolve().parents[1]
    / "artefacts"
    / "weights"
    / "bert_base_finetuned.pt"
)

MODEL_NAME = "bert-base-uncased"
_TOKENIZER = AutoTokenizer.from_pretrained(MODEL_NAME)


def _load_model():
    """Return a CPU-loaded, eval-mode model with your saved weights."""
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME, num_labels=2
    )
    state = torch.load(WEIGHTS, map_location="cpu")
    model.load_state_dict(state)
    model.eval()
    return model


def predict(texts):
    """
    texts : list[str]  – raw English reviews
    returns : list[int] – 0 = negative, 1 = positive
    """
    enc = _TOKENIZER(
        texts,
        padding=True,
        truncation=True,
        max_length=128,
        return_tensors="pt",
    )
    with torch.no_grad():
        logits = _load_model()(**enc).logits
    return logits.argmax(1).tolist()
