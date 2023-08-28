#!/usr/bin/env python3
"""measures the total execution time for wait_n"""
import time
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps d'exécution moyen de wait_n(n, max_delay).

    Args:
        n (int): Le nombre de fois à appeler wait_n.
        max_delay (int): Le délai maximum en secondes pour
        chaque appel à wait_n.

    Returns:
        float: Le temps d'exécution moyen par appel en secondes.
    """
    start_time = time.time()
    await asyncio.gather(*(wait_n(max_delay) for _ in range(n)))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
