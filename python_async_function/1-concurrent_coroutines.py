#!/usr/bin/env python3
"""
This module extends the asynchronous capabilities to execute multiple
coroutines concurrently and return sorted delays.
"""

import asyncio
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Execute multiple instances of wait_random concurrently.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
