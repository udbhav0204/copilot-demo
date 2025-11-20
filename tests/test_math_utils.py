import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.math_utils import add, subtract, is_even

def test_add():
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False
