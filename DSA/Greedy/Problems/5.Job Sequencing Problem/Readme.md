### Problem

Given `N` jobs, each with a **deadline** and **profit**. Each job takes 1 unit of time. Maximize profit while scheduling jobs such that each job is completed before its deadline.

### Greedy Strategy

1. Sort jobs by **profit descending**.
2. For each job, schedule it in the **latest available slot ≤ deadline**.
3. Track:
   - Number of jobs done.
   - Total profit.

---

### 📌 Example

```python
python
CopyEdit
Jobs = [[1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15]]
# Output: [2, 127]  -> Jobs 1 and 3 selected

```

---

### ⚠️ Constraints

- `1 <= N <= 10^4`
- `1 <= Deadline <= N`
- `1 <= Profit <= 500`

---

## 🔄 Time & Space Complexity

| Part                       | Complexity                      |
| -------------------------- | ------------------------------- |
| Sorting Jobs               | O(N log N)                      |
| Scheduling (in worst case) | O(N × D) where D = max deadline |
| Space                      | O(D)                            |
