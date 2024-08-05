#!/usr/bin/env python3
"""Module for task_wait_n function"""
import asyncio
from typing import List
from 3_tasks import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the wait_random n times."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
