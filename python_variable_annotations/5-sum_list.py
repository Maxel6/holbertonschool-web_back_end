#!/usr/bin/env python3
"""Computes the sum of a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the elements in the list as a float.
    """
    return sum(input_list)
