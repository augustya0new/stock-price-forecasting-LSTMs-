from src.models import TransformerTimeSeries

def test_model():
    model = TransformerTimeSeries(5, 64, 2, 1)
    assert model is not None

test_model()
