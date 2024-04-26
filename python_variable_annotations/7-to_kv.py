#!/usr/bin/env python3
"""
This module provides a function that takes a string and a number, and returns
a tuple with the string and the square of the number.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple containing a string and the square of a number.
    """
    return (k, float(v ** 2))
