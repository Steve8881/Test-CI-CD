"""
Utilities for basic mathematical operations.

This module provides several functions for basic arithmetic, including
addition, subtraction, multiplication, and division.

Attributes
----------
PI : float
    The mathematical constant π, approximately equal to 3.14159.

Examples
--------
>>> add_numbers(1, 2)
3
>>> subtract_numbers(4, 2)
2

"""


def addNumbers(a, b):
    """
    Adds two numbers.

    Parameters
    ----------
    a : int or float
        The first number to add.
    b : int or float
        The second number to add.

    Returns
    -------
    int or float
        The sum of `a` and `b`.

    Raises
    ------
    TypeError
        If either `a` or `b` is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers.")
    return a + b


def mulNumbers(a, b):
    """
    Adds two numbers.

    Parameters
    ----------
    a : int or float
        The first number to add.
    b : int or float
        The second number to add.

    Returns
    -------
    int or float
        The sum of `a` and `b`.

    Raises
    ------
    TypeError
        If either `a` or `b` is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers.")
    return a * b


addNumbers(1, 2)
mulNumbers(1, 2)
