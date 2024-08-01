#!/usr/bin/env python3
"""
This module is complex types - functions
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float
    """
    def multiplies(n: float):
        """
        multiply two number
        """
        return n * multiplier

    return multiplies
