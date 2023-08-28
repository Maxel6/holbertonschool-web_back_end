#!/usr/bin/env python3
"""
takes a string k and an int OR float
v as arguments and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with the string k and the square of v as a float.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple containing k and the square of v as a float.
    """
    squared_value = float(v) ** 2
    return k, squared_value
