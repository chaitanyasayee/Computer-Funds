## Problem 1: Minimum Number of Jumps to Reach End

> Given an array nums, where each element represents the maximum jump length from that position, return the minimum number of jumps needed to reach the last index.

---

### Greedy Idea (with Range Tracking)

- Track the **farthest reachable index** so far.
- Maintain the **current range** of the current jump.
- When you reach the end of the current range, **increment the jump count** and update the range.

---

### Python Code – Min Jumps

```python
def min_jumps(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):  # exclude last index
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps

```

---

### Example

```python
nums = [2, 3, 1, 1, 4]
# Output: 2 (0 → 1 → 4)

```

---

## Problem 2: Return the Path (Jump Indices)

> Instead of only counting jumps, now we want to return the actual indices from which each jump is made (i.e., the path taken).

---

### Strategy

- Extend the greedy approach to **record jump start positions**.
- Keep track of the **previous jump index**.
- When we make a jump (i.e., when `i == current_end`), **append the index to the path**.
- At the end, add the last index (destination).

---

### Python Code – Return Path

```python
def jump_path(nums):
    n = len(nums)
    if n <= 1:
        return [0]

    path = [0]
    current_end = 0
    farthest = 0
    last_jump_index = 0

    for i in range(n - 1):
        if i + nums[i] > farthest:
            farthest = i + nums[i]
            next_jump_index = i

        if i == current_end:
            last_jump_index = next_jump_index
            path.append(last_jump_index)
            current_end = farthest

    # Ensure path ends at last index
    if path[-1] != n - 1:
        path.append(n - 1)

    return path

```

---

### Example

```python
nums = [2, 3, 1, 1, 4]
# Output: [0, 1, 4]
# Jumps: 0 → 1 → 4

```

---

### Time and Space Complexity

| Metric | Value           |
| ------ | --------------- |
| Time   | O(n)            |
| Space  | O(n) — for path |

---

## Summary

| Task                    | Approach Summary                        |
| ----------------------- | --------------------------------------- |
| Min jumps to reach end  | Greedy with range tracking, count jumps |
| Path of jumps (indices) | Track and store indices of each jump    |
