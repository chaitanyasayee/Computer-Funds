### Problem Statement:

Given the **arrival** and **departure** times of `N` trains at a railway station, find the **minimum number of platforms** required so that **no train has to wait** for a platform.

> A platform cannot be shared between an arriving and departing train at the same time.

### Constraints:

- `1 <= N <= 10⁵`
- `0000 <= Arrival[i] <= Departure[i] <= 2359`
- Time is in 24-hour format without `:` (e.g., 0900 = 9:00 AM)

---

### Intuition:

If multiple trains are **at the station at the same time**, we need multiple platforms. The idea is to **track the number of overlapping trains** at any moment, and return the **maximum number of overlaps** (i.e., platforms needed).

---

## Brute Force Approach

### Approach:

- For each train, check how many other trains **overlap** with it (i.e., are at the station at the same time).
- Keep track of the **maximum overlaps**.

### Code (Python):

```python
def findPlatform(arr, dep, n):
    max_platforms = 1
    for i in range(n):
        count = 1
        for j in range(i + 1, n):
            if (arr[i] >= arr[j] and arr[i] <= dep[j]) or (arr[j] >= arr[i] and arr[j] <= dep[i]):
                count += 1
        max_platforms = max(max_platforms, count)
    return max_platforms

```

### Time Complexity:

- **O(N²)** – nested comparisons

### Space Complexity:

- **O(1)** – no extra space

---

## Optimal Greedy + Sorting Approach

### Approach:

1. Sort both **arrival** and **departure** times.
2. Use **two pointers**:
   - One for `arr[]` and one for `dep[]`
3. Traverse and:
   - If `arr[i] <= dep[j]`: One train arrives before another departs → Need **+1 platform**
   - Else: One train departs before the next arrives → **Free one platform**
4. Track the **maximum platforms needed**.

### Dry Run:

**Input:**

```
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

```

**Sorted:**

```
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1120, 1130, 1200, 1900, 2000]

```

Walk through with two pointers → count how many are in station simultaneously.

## Complexity Analysis

| Approach    | Time Complexity | Space Complexity |
| ----------- | --------------- | ---------------- |
| Brute Force | O(N²)           | O(1)             |
| ✅ Optimal  | O(N log N)      | O(1)             |

---

## Summary

| Feature                  | Brute Force | Optimal Greedy            |
| ------------------------ | ----------- | ------------------------- |
| Sorting                  | ❌ No       | ✅ Yes                    |
| Two-Pointer Technique    | ❌ No       | ✅ Yes                    |
| Suitable for large input | ❌ No       | ✅ Yes (Up to 10⁵ trains) |
| Time Complexity          | O(N²)       | ✅ O(N log N)             |
