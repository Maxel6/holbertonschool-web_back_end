#!/usr/bin/env python3
"""
        The coroutine will loop 10 times,
        each time asynchronously wait 1 second, then yield a
        random number between 0 and 10.
    """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous coroutine that yields random numbers between 0 and 10.

    This coroutine loops 10 times each time asynchronously waiting for 1 second
    and then yielding a random number between 0 and 10 using the random module.

    Yields:
        int: A random integer between 0 and 10.

    Usage:
        async for num in async_generator():
            print(num)
    """
    for _ in range(10):
        yield random.uniform(1, 10)
        await asyncio.sleep(1)
