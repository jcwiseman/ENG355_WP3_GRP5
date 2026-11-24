"""Animal math functions.

Every function in this file that doesn't start with an underscore is available
at /api/<function name>. Arguments arrive as strings. Raise ValueError to send
an error message back to the user.
"""

_SQUARE_ROOTS = {
    "cat": "kitten",
    "dog": "puppy",
    "cow": "calf",
}


def sqrt(animal):
    """Return the square root of an animal (its baby)."""
    animal = animal.strip().lower()
    if animal not in _SQUARE_ROOTS:
        raise ValueError(f"'{animal}' has no known square root")
    return _SQUARE_ROOTS[animal]


def add(a, b):
    """Add two animals together."""
    return f"{a.strip().lower()}-{b.strip().lower()}"
