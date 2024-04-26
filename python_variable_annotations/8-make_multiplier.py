#!/usr/bin/env python3
"""
This module provides a function that returns another function, which
multiplies a given number by a preset multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies any float by a given
    multiplier.
    """
    def multiplier_func(number: float) -> float:
        return number * multiplier

    return multiplier_func
