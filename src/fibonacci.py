"""
Holds the fibonacci algorithm.
"""

from functools import lru_cache


@lru_cache
def fibonacci(num: int) -> int:
    """
    Calculate result of the fibonacci sequence:
    f 0, 1, 2, 3, 4, 5,...,10
    v 0, 1, 1, 2, 3, 5,...,55

    Arg:
        num(int): The number to calculate.

    Returns:
        The result of f(n) = f(n - 1) + f(n - 2)
    """
    if num ==0:
        return 0
    
    if num <= 2:
        return 1
    
    return fibonacci(num - 1) + fibonacci(num - 2)