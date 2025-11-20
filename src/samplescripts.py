def add(a, b):
    """Add two numbers.
    Compute the arithmetic sum of two numeric inputs.
    Args:
        a (int | float): The first addend.
        b (int | float): The second addend.
    Returns:
        int | float: The sum of a and b.
    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 1.5)
        4.0
    """
    """Subtract one number from another.
    Return the result of subtracting b from a.
    Args:
        a (int | float): The minuend.
        b (int | float): The subtrahend.
    Returns:
        int | float: The result of a - b.
    Examples:
        >>> subtract(5, 2)
        3
        >>> subtract(2.5, 1.0)
        1.5
    """
    """Multiply two numbers.
    Compute the product of two numeric inputs.
    Args:
        a (int | float): The first factor.
        b (int | float): The second factor.
    Returns:
        int | float: The product of a and b.
    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(2.5, 2)
        5.0
    """
    """Divide one number by another.
    Return the quotient of a divided by b. This function performs true division
    and will return a float when appropriate.
    Args:
        a (int | float): The dividend.
        b (int | float): The divisor.
    Returns:
        float: The result of a / b.
    Raises:
        ZeroDivisionError: If b is zero.
    Examples:
        >>> divide(6, 3)
        2.0
        >>> divide(7, 2)
        3.5
    """
    """Determine if an integer is even.
    Check whether the provided integer is evenly divisible by 2.
    Args:
        n (int): The integer to check. Behavior is defined for integers; if a
            non-integer is provided, the result depends on Python's modulo behavior.
    Returns:
        bool: True if n is even (n % 2 == 0), False otherwise.
    Examples:
        >>> is_even(4)
        True
        >>> is_even(3)
        False
    """
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def is_even(n):
    return n % 2 == 0
