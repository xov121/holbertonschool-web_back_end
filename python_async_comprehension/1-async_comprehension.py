#!/usr/bin/env python3
"""
This module uses an async comprehension to collect random numbers from
an asynchronous generator.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collect 10 random numbers using an async comprehension from
    the async_generator.
    """
    return [i async for i in async_generator()]
