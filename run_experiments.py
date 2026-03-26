# run_experiments.py
"""
Run timing experiments across sorting algorithms and datasets.
Generates results.csv and prints a compact table.

Important:
 - For QuickSort (last-element pivot), worst-case recursion depth can be O(n).
   Python's default recursion limit (~1000) may be exceeded for large worst-case inputs.
   This script raises recursionlimit to a safe value.
"""

import sys
import copy
import csv
from pprint import pprint

# raise recursion limit for QuickSort on degenerate inputs
sys.setrecursionlimit(30000)

from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from utils.timing import time_function
from dataset_gen import generate_all

ALGORITHMS = {
    "InsertionSort": {
        "func": insertion_sort,
        "inplace": True
    },
    "MergeSort": {
        "func": merge_sort,
        "inplace": False  # returns new list
    },
    "QuickSort": {
        "func": quick_sort,
        "inplace": True
    }
}

DATASET_TYPES = ["random", "sorted", "reverse"]
SIZES = (1000, 5000, 10000)
REPEATS = 3  # number of repeats to average timing

def run():
    datasets = generate_all(SIZES, seed=42)
    results = []  # rows: algorithm, dataset_type, size, avg_time_seconds

    print("Starting experiments. Sizes:", SIZES)
    for algo_name, meta in ALGORITHMS.items():
        func = meta["func"]
        inplace = meta["inplace"]
        print(f"\n=== Algorithm: {algo_name} (inplace={inplace}) ===")
        for dtype in DATASET_TYPES:
            for n in SIZES:
                base = datasets[dtype][n]
                # run repeats; for in-place sorters pass copies each repeat
                def run_once():
                    if inplace:
                        arr = copy.deepcopy(base)
                        func(arr)
                        return None
                    else:
                        # func returns a new list
                        res = func(list(base))
                        return res

                avg_time, _ = time_function(run_once, repeats=REPEATS)
                print(f"{algo_name:12s} | {dtype:7s} | n={n:5d} -> {avg_time:.6f} s (avg of {REPEATS})")
                results.append({
                    "algorithm": algo_name,
                    "dataset": dtype,
                    "size": n,
                    "avg_time_s": f"{avg_time:.6f}"
                })

    # write CSV
    csv_path = "results.csv"
    with open(csv_path, "w", newline="") as csvfile:
        fieldnames = ["algorithm", "dataset", "size", "avg_time_s"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow(r)

    print(f"\nExperiments completed. Results written to {csv_path}.\nSample rows:")
    pprint(results[:6])

if __name__ == "__main__":
    run()