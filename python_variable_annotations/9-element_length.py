#!/usr/bin/env python3
"""Computes the sum of a list of floats."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    
    Each tuple contains the original sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples wherex
        each tuple contains
        a sequence from lst and its length as an integer.
    """
    return [(i, len(i)) for i in lst]
