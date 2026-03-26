# Lab Task 3: Sorting Algorithms – Performance & Trade-offs
Name: <Your Name>  
Course: <Course Name>  
Date: <Date>

---

## 1. Introduction

This lab implements and compares three sorting algorithms:

- Insertion Sort
- Merge Sort
- Quick Sort (Lomuto partition, last element as pivot)

The goal is to experimentally measure performance on different input types and compare the results with theoretical time complexities.

Datasets tested:
- Random lists (1000, 5000, 10000 elements)
- Already sorted lists (1000, 5000, 10000 elements)
- Reverse-sorted lists (1000, 5000, 10000 elements)

Execution time was averaged over 3 runs for each configuration.

---

## 2. Theoretical Time Complexities

| Algorithm       | Best Case     | Average Case   | Worst Case     | Stable | In-Place |
|---------------|--------------|--------------|--------------|--------|----------|
| InsertionSort | O(n)         | O(n²)        | O(n²)        | Yes    | Yes      |
| MergeSort     | O(n log n)   | O(n log n)   | O(n log n)   | Yes    | No       |
| QuickSort     | O(n log n)   | O(n log n)   | O(n²)        | No     | Yes      |

---

## 3. Experimental Observations

### 3.1 Insertion Sort

- Performed very well on already sorted lists (near linear time).
- Performance degraded significantly for random and reverse lists as input size increased.
- Execution time increased roughly quadratically.
- Suitable for small datasets or nearly sorted data.

### 3.2 Merge Sort

- Showed consistent performance across all dataset types.
- Execution time increased approximately proportional to n log n.
- Stable and predictable.
- Required additional memory (not in-place).

### 3.3 Quick Sort (Last Element Pivot)

- Performed well on random datasets.
- Performance degraded noticeably on sorted and reverse-sorted datasets.
- This matches theoretical worst-case O(n²) behavior when pivot choice is poor.
- Recursive depth increased significantly for sorted inputs.
- In-place but not stable.

---

## 4. Alignment with Theory

The experimental results closely match theoretical expectations:

- Insertion Sort showed quadratic growth for large random inputs.
- Merge Sort maintained stable O(n log n) behavior across all input types.
- Quick Sort demonstrated worst-case behavior on sorted and reverse inputs due to fixed pivot selection (last element).

Thus, the practical measurements validate the theoretical time complexity analysis.

---

## 5. Stability and In-Place Analysis

### Insertion Sort
- Stable ✔
- In-place ✔
- Good for small or nearly sorted datasets.

### Merge Sort
- Stable ✔
- Not in-place ✘ (requires auxiliary array)
- Reliable and predictable performance.

### Quick Sort
- Not stable ✘
- In-place ✔
- Efficient on average, but sensitive to pivot selection.

---

## 6. Trade-offs Discussion

- Insertion Sort is simple and efficient for small datasets but scales poorly.
- Merge Sort guarantees O(n log n) time but uses extra memory.
- Quick Sort is generally fastest in practice but can degrade badly without a good pivot strategy.

A randomized pivot or median-of-three strategy would reduce the chance of worst-case behavior in Quick Sort.

---

## 7. Conclusion

This experiment demonstrates that:

- Theoretical complexity strongly predicts practical performance.
- Dataset characteristics significantly affect algorithm efficiency.
- Quick Sort requires careful pivot selection.
- Merge Sort offers stable and consistent performance.
- Insertion Sort is suitable only for small or nearly sorted inputs.

Overall, Merge Sort provides the most consistent behavior, while Quick Sort is often fastest on average but less predictable.

---

## 8. Reproducibility

To reproduce results:
