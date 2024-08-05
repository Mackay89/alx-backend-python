#!/usr/bin/env python3
"""
This module contains the asynchronous coroutine wait_random.
"""


import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[float, int]:
    """
    Asynchronous coroutine function that waits 'max_delay'
    for a random delayed number.


    Args:
      max_delay (int): The maximum delay in seconds (default is 10).


    Returns:
      float: The random delay value.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

