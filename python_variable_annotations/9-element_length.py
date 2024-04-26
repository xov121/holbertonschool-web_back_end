#!/usr/bin/env python3
"""
This module provides a function that returns a list of tuples, each containing
an element from an iterable and its length.
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple contains an element from the
    iterable and its length.
    """
    return [(i, len(i)) for i in lst]
