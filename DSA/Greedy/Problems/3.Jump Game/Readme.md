### Problem Statement

You are given an array of integers `nums`, where each element `nums[i]` represents the **maximum number of steps** you can jump forward from index `i`.

Starting from the **first index (index 0)**, determine if it is possible to reach the **last index** of the array.

Return `true` if the last index can be reached, otherwise return `false`.

### Input

- `nums`: an integer array of length `n`
  - `1 <= nums.length <= 10⁴`
  - `0 <= nums[i] <= 10⁴`

### Output

- A boolean value: `true` if the end is reachable, otherwise `false`

### Greedy Approach

1. Keep track of the **farthest index** you can reach so far.
2. At each index `i`, if `i > farthest`, it means you cannot proceed further — return `false`.
3. Otherwise, update `farthest = max(farthest, i + nums[i])`.
4. If you complete the loop, return `true`.

---

### Algorithm (Python)

```python
def can_jump(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
    return True

```

---

### Example 1

```
Input: [2, 3, 1, 1, 4]
Output: true

Explanation:
Start at index 0:
- Jump 1 → index 1
- Jump 1 → index 2
- Jump 1 → index 3
- Jump 1 → index 4
You can reach the last index.

```

---

### Example 2

```
Input: [3, 2, 1, 0, 4]
Output: false

Explanation:
You reach index 3, but nums[3] = 0, so you can't go further.

```

---

### Example 3

```
Input: [5, 3, 2, 1, 0]
Output: true

Explanation:
From index 0, you can directly jump beyond the last index.

```

---

### Time and Space Complexity

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |
