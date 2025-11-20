# Copilot Buggy Suggestion Example

from numbers import Number

def calculate_average(numbers):
    """
    Calculate the arithmetic mean of numeric values in 'numbers'.

    This function validates that `numbers` is an iterable containing at least one
    numeric value and raises clear exceptions for invalid input to avoid
    ZeroDivisionError or TypeError from unexpected values.

    Raises:
        TypeError: if `numbers` is not iterable or contains non-numeric items.
        ValueError: if `numbers` is empty or contains no numeric values.
    """
    try:
        seq = list(numbers)
    except TypeError:
        raise TypeError("calculate_average expects an iterable of numeric values")

    if not seq:
        raise ValueError("calculate_average requires at least one numeric value")

    # Ensure every item is a real number
    for i, v in enumerate(seq):
        if not isinstance(v, Number):
            raise TypeError(f"non-numeric value at index {i}: {v!r}")

    total = sum(seq)
    return total / len(seq)
