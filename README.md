# Lab 3 — Sorting Algorithms: Performance & Trade-offs

## Files
- `sorting/`:
  - `insertion_sort.py` — in-place stable insertion sort
  - `merge_sort.py` — merge sort (returns new list)
  - `quick_sort.py` — in-place quicksort using last element as pivot (Lomuto)
- `dataset_gen.py` — generates random, sorted, reverse lists (1000,5000,10000)
- `utils/timing.py` — timing helper (averages repeats)
- `run_experiments.py` — runs experiment matrix and writes `results.csv`
- `report.md` — suggested short report/analysis

## How to run
1. Ensure Python 3.8+ installed.
2. From project root:
```bash
python3 run_experiments.py