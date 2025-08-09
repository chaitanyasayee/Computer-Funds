### **Problem Statement**

You are given `N` meetings in the form of two arrays `start[]` and `end[]`:

- `start[i]` denotes the start time of the `i-th` meeting.
- `end[i]` denotes the end time of the `i-th` meeting.

You have **only one meeting room**. Determine the **maximum number of meetings** that can be accommodated **without overlapping**.

### **Constraints**

- `1 ≤ N ≤ 10⁵`
- `0 ≤ start[i] < end[i] ≤ 10⁵`

---

### **Examples**

**Example 1**

Input:

`start = [1, 3, 0, 5, 8, 5]`

`end = [2, 4, 6, 7, 9, 9]`

Output: `4`

Explanation: The meetings (1,2), (3,4), (5,7), (8,9) can be scheduled.

**Example 2**

Input:

`start = [10, 12, 20]`

`end = [20, 25, 30]`

Output: `1`

Explanation: Only one meeting can be scheduled.

**Example 3**

Input:

`start = [1, 4, 6, 9]`

`end = [2, 5, 7, 12]`

Output: `4`

---

### Brute Force Logic:

1. Generate all subsets of the meetings.
2. For each subset:
   - Sort by start time.
   - Check if any meetings in the subset overlap.
   - Keep track of the largest non-overlapping subset.

---

---

### Time Complexity

- **Time:** `O(2^N * N log N)` → very inefficient for large `N`
- **Space:** `O(N)`

---

### **Optimal Greedy Approach**

1. Pair start and end times as `(end[i], start[i])` for each meeting.
2. Sort the meetings by their **end time**.
3. Initialize `count = 1`, and `last_end = end of the first meeting`.
4. Iterate through sorted meetings:
   - If `start[i] > last_end`, increment count and update `last_end`.

**Why Greedy?**

To fit the **maximum** number of meetings, always choose the **meeting that ends earliest**.

---

### **Time & Space Complexity**

- **Time**: `O(N log N)` for sorting.
- **Space**: `O(N)` for storing meetings (can be `O(1)` if done in-place).
