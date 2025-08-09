## Problem Statement

You are given a list of **non-overlapping**, **sorted** intervals (by start time). Given a new interval, insert it into the correct position and **merge if necessary** to maintain the list as non-overlapping and sorted.

---

### Input

- `Intervals`: List of intervals `[start, end]` (non-overlapping & sorted).
- `newInterval`: A new interval to insert.

---

### Output

- Updated list of merged and sorted intervals.

---

### Examples

### Example 1

```
Input: Intervals = [[1,3], [6,9]], newInterval = [2,5]
Output: [[1,5], [6,9]]

```

### Example 2

```
Input: Intervals = [[1,2], [3,5], [6,7], [8,10]], newInterval = [4,8]
Output: [[1,2], [3,10]]

```

### Example 3

```
Input: Intervals = [], newInterval = [4,8]
Output: [[4,8]]

```

---

## Constraints

- `0 <= Intervals.length <= 10⁵`
- `0 <= start[i] < end[i] <= 10⁷`
- `0 <= start < end <= 10⁷`
- `Intervals[i].length == 2`
- `newInterval.length == 2`

---

## Approaches

### Brute Force Approach

### Idea:

- Add the `newInterval` to the list.
- Sort all intervals.
- Merge them like the standard merge-intervals problem.

### Time Complexity:

- **O(n log n)** for sorting
- **O(n)** for merging
- Overall: **O(n log n)**

---

### Optimal Greedy Approach

### Intuition:

Since intervals are already **sorted** and **non-overlapping**, we:

1. Add all intervals that end **before** `newInterval` (no overlap).
2. Merge all overlapping intervals.
3. Add all intervals that start **after** `newInterval`.

### Time Complexity:

- **O(n)** — one pass through the list.

## Summary

| Aspect           | Brute Force           | Optimal Greedy          |
| ---------------- | --------------------- | ----------------------- |
| Time Complexity  | `O(n log n)`          | `O(n)`                  |
| Space Complexity | `O(n)`                | `O(n)`                  |
| Suitable for     | Small to Medium Input | Large Input (`n ≤ 10⁵`) |
| Key Insight      | Sort & Merge          | Skip → Merge → Append   |
