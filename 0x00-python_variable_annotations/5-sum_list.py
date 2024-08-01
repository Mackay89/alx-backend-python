#!/usr/bin/env python3
"""
This module Contains a single function sum_list that sums a list of floats and returns the result.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats and returns the result.


    Args:
      input_list (list[float]): The list of floats to be summed.


    Returns:
      float: The sum of the list of floats.
    """

    return sum(input_list)
