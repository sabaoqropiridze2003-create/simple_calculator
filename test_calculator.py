import pytest


from calculator import add, divide, subtract, multiply

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(10, 5) == 7


def test_multiply():
    assert multiply(2, 5) == 10

def test_divide():
    assert divide(12, 3) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
