from src.example1 import multiplier


def test_multiplier():
    assert multiplier(5, 4) == 20


def test_multiplier_none():
    assert not multiplier(None, 4)
