#!/usr/bin/env python3
"""
This module contains a single function to_kv that returns a tuple containing a
string and the square of an int or float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
      """
      Returns a tuple with a string and the square of the given number.
      """

      return (k, float(v**2))
