#!/usr/bin/env python3
"""Module for task_wait_random function"""
import asyncio
from basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio.Task for wait_random with max_delay."""
    return asyncio.create_task(wait_random(max_delay))

