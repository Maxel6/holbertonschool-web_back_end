#!/usr/bin/env python3
"""A module with a asynchronous generator"""

import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous function that uses an asynchronous comprehension
    to collect 10 numbers generated asynchronously from 'async_generator'
    and returns them in a list.

    Returns:
        List[float]: A list of floating-point numbers.
    """
    return [i async for i in async_generator()]
