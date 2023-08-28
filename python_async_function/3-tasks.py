#!/usr/bin/env python3
"""returns a asyncio.Task."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that runs wait_random(max_delay).

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio.Task that runs wait_random(max_delay).
    """
    task = asyncio.ensure_future(wait_random(max_delay))
    return task
