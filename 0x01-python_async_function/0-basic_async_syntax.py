#!/usr/bin/env python3
"""
This module contains the asynchronous coroutine wait_random.
"""


import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).
        
    Returns:
        float: The random delay value.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay

