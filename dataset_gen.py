# dataset_gen.py
"""
Generate datasets needed for experiments:
 - random list (seeded)
 - already sorted list
 - reverse-sorted list
for sizes: e.g., 1000, 5000, 10000
"""

import random
from typing import List, Dict

def gen_random_list(n: int, seed: int = 0) -> List[int]:
    rnd = random.Random(seed)
    # generate integers in range 0..n*10 for variety
    return [rnd.randint(0, n * 10) for _ in range(n)]

def gen_sorted_list(n: int) -> List[int]:
    return list(range(n))

def gen_reverse_list(n: int) -> List[int]:
    return list(range(n - 1, -1, -1))

def generate_all(sizes=(1000, 5000, 10000), seed=0) -> Dict[str, Dict[int, List[int]]]:
    """
    Returns structure:
    {
      "random": {size: [...], ...},
      "sorted": {size: [...], ...},
      "reverse": {size: [...], ...}
    }
    """
    out = {"random": {}, "sorted": {}, "reverse": {}}
    for n in sizes:
        out["random"][n] = gen_random_list(n, seed=seed)  # same seed makes reproducible
        out["sorted"][n] = gen_sorted_list(n)
        out["reverse"][n] = gen_reverse_list(n)
    return out