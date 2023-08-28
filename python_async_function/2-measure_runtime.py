#!/usr/bin/env python3
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n
"""measures the total execution time for wait_n"""


def measure_time(n: int, max_delay: int) -> float:
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

    for _ in range(n):
        wait_n(n, max_delay)

    end_time = time.time()

    return (end_time - start_time)/n
