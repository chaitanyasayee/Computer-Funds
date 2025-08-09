## Problem Statement

Given an array of intervals, return the **minimum number of intervals you need to remove** to make the rest of the intervals **non-overlapping**.

---

## Constraints

- `1 <= intervals.length <= 10⁵`
- `0 <= start[i] < end[i] <= 10⁵`
- `intervals[i].length == 2`

---

## Approach

### Brute Force

- Try removing each interval and check if the rest are non-overlapping.
- For each possible removal, check all remaining intervals for overlaps.
- This is **not feasible for large input sizes**.

### Time Complexity:

- **O(N²)** – Too slow for `N ≈ 10⁵`

---

### Optimal Greedy Approach

### Intuition:

- Sort intervals by their **ending time**.
- Always pick the interval that ends earliest (to leave room for others).
- Count the number of non-overlapping intervals.
- Subtract that from the total to get the number of intervals to remove.

### Steps:

1. Sort intervals by `end`.
2. Initialize `limit = -∞`, `count = 0`.
3. For each interval:
   - If `start >= limit`, increment `count`, update `limit = end`.
4. Return `total - count`

## Time and Space Complexity

| Approach       | Time Complexity       | Space Complexity |
| -------------- | --------------------- | ---------------- |
| Brute Force    | O(2ⁿ \* n)            | O(n)             |
| Greedy Optimal | **O(n log n)** (sort) | O(1)             |
