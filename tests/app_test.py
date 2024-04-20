"""
Testing Fibonnaci functionality.
"""
import pytest
from typing import Any
from app import fibonacci, input_is_valid


@pytest.mark.parametrize(
        "value, expected",
        [
            (0, 0),
            (1, 1),
            (10, 55),
            (19, 4181),
        ]
)
def test_fibonacci(value: int, expected: int) -> None:
    """
    Ensures that values work as expected.
    
    Happy case.

    Args:
        value (Any): The value to test.
        expected (int): The value we expect.
    """
    assert fibonacci(value) == expected


@pytest.mark.parametrize(
        "value, expected",
        [
            ("0", True),
            ("1", True),
            ("x", False),
        ]
)
def test_input_is_valid(value: Any, expected: bool) -> None:
    """
    Test that validator is filtering correctly.

    Args:
        value (Any): The value to test.
        expected (bool): The value we expect.
    """
    assert input_is_valid(value) is expected
