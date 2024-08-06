#!/usr/bin/env python3
"""A coroutine called async_generator that takes no arguments."""
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator that yields random numbers between 0 and 10.
    It yields a random number 10 times with a 1 second delay between each yield.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

