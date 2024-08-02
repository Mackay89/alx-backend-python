#!/usr/bin/env python
"""
 Type Checking
"""


from typing import Union, Any, Mapping, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on the elements of the input tuple by the given factor.


    Args:
        lst (Tuple): The input tuple.
        factor (int, optional): The zoom factor. Defaults to 2.


    Returns:
        List[Any]: The zoomed-in list
    """

    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)


zoom_2x = zoom_array(array)


zoom_3x = zoom_array(array, 3)

