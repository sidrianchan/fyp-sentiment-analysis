import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))   # ← add project root
from src.infer import predict

def test_bert_inference():
    sample = ["Great taste!", "Terrible service."]
    preds  = predict(sample)
    assert len(preds) == 2
    # sanity: expect the two predictions to differ
    assert preds[0] != preds[1]
