#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Measures the total runtime for executing async_comprehension four times in parallel."""
    start_time = time.time()
    
    # Run async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = time.time()
    return end_time - start_time

