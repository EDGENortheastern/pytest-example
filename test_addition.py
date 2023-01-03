import pytest

from addition import addition

def test_addition():
    assert addition(2,2) == 4

def test_addition_neg():
    assert addition(-2,-2) == -5