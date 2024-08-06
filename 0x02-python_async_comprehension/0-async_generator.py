#!/usr/bin/env python3
"""
Module that contains an async generator coroutine.
"""

import asyncio
import random
from typing import AsyncIterator

async def async_generator() -> AsyncIterator[float]:
    """
    Async generator that yields random numbers between 0 and 10 with a 
    1-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

