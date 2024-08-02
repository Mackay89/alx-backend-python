#!/usr/bin/env python3
"""
 More involved type annotations
"""


from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
        """
        Safely get value


        Args:
             dct (Mapping[Any, T]): The dictionary to retrieve the value from.
             key (Any): The key to look up in the dictionary.
             default (Union[T, None], optional): The default value to return if the key is not found. Defaults to None.


        Returns:
            Union[T, None]: The value associated with the key in the dictionary or the default value if the key is not found.
        """
        if key in dct:
            return dct[key]
        else:
            return default
