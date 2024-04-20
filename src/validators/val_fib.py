
"""
Holds validation functions.
"""

def input_is_valid(num: str) -> bool:
    """
    Validate if the given input is valid.

    Also makes a good injection point for validations and parameter 
    sanitization.
    """
    is_valid = False
    try:
        int(num)
        is_valid = True
    except ValueError:
        pass
    return is_valid
