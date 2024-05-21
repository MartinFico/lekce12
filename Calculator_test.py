import pytest
from My_modul import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_subtract(calc):
    assert calc.subtract(7, 2) == 5

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12

def test_divide(calc):
    assert calc.divide(10, 2) == 5.0
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_maximum(calc):
    assert calc.maximum(2, 3) == 3

def test_minimum(calc):
    assert calc.minimum(2, 3) == 2

def test_percentage(calc):
    assert calc.percentage(20, 50) == 40.0
    with pytest.raises(ValueError):
        calc.percentage(20, 0)
