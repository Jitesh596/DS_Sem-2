# utils/timing.py
"""
Timing helper: run function multiple times and return average elapsed time.
"""

import time
from typing import Callable, Any, Tuple

def time_function(func: Callable, *args, repeats: int = 3, **kwargs) -> Tuple[float, Any]:
    """
    Runs func(*args, **kwargs) `repeats` times and returns (avg_seconds, last_result).
    For in-place sorters, func should mutate its first argument; result returned is None.
    NOTE: Caller should pass copies of inputs to preserve original data across repeats.
    """
    if repeats <= 0:
        repeats = 1
    durations = []
    last_res = None
    for _ in range(repeats):
        start = time.perf_counter()
        last_res = func(*args, **kwargs)
        end = time.perf_counter()
        durations.append(end - start)
    avg = sum(durations) / len(durations)
    return avg, last_res