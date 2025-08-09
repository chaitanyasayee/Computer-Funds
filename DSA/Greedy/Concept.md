# What is a Greedy Algorithm?

A **Greedy Algorithm** is an approach where we **make the locally optimal choice at each step**, hoping that this leads to a globally optimal solution.

> In simple words: "Take the best you can get right now, without worrying about the future."

---

## Key Idea

- Greedy chooses the best option at the **current moment**.
- It **doesn’t reconsider** decisions made earlier.
- Works **only** when the **problem has the _Greedy Choice Property_ and _Optimal Substructure_**.

---

## Important Terms

| Term                       | Explanation                                                                    |
| -------------------------- | ------------------------------------------------------------------------------ |
| **Greedy Choice Property** | A global optimum can be reached by choosing a local optimum.                   |
| **Optimal Substructure**   | Optimal solution to the problem contains optimal solutions to its subproblems. |

---

## When to Use Greedy?

Use it when:

- You can **sort the input** and decide in a specific order.
- The problem **asks for max/min value** (e.g., max profit, min cost).
- You can **prove** that your local choices lead to the best global answer.

---

## Common Greedy Pattern

1. **Sort the input** (if needed).
2. Iterate through input:
   - At each step, pick the **best current option**.
   - Update result/state.
3. Return the final answer.

---

## Greedy vs. Dynamic Programming

| Greedy                      | Dynamic Programming            |
| --------------------------- | ------------------------------ |
| Makes local optimal choice  | Explores all possible choices  |
| Faster (Usually O(n log n)) | Slower (Usually O(n²) or more) |
| No backtracking             | Uses memoization or tabulation |
| Doesn't always work         | Always works if applicable     |

---

## Classic Greedy Algorithm Problems

| Problem                   | Description                                   | Key Idea                                     |
| ------------------------- | --------------------------------------------- | -------------------------------------------- |
| **Activity Selection**    | Maximize number of non-overlapping activities | Sort by end time                             |
| **Fractional Knapsack**   | Maximize value for given capacity             | Sort by value/weight                         |
| **Job Sequencing**        | Max profit by scheduling jobs with deadlines  | Sort by profit, use slot                     |
| **Huffman Encoding**      | Minimize cost of encoding characters          | Use priority queue                           |
| **Minimum Spanning Tree** | Connect all nodes with minimum cost           | Kruskal’s / Prim’s Algorithm                 |
| **Dijkstra’s Algorithm**  | Shortest path from source                     | Use priority queue, greedy pick min distance |

---

## Examples

---

### Activity Selection Problem

**Input:**

Start = [1, 3, 0, 5, 8, 5]

End = [2, 4, 6, 7, 9, 9]

**Idea:**

- Sort activities by **end time**
- Select the first activity
- For remaining activities, pick if **start time > last selected end time**

```cpp
// C++ like logic
sort by end time
last_end = 0
count = 0
for each activity:
    if activity.start >= last_end:
        select it
        last_end = activity.end

```

---

### 🔸 Fractional Knapsack Problem

**Input:**

Items with value and weight, total capacity = W

**Idea:**

- Sort items by **value/weight** ratio
- Take as much as possible from each item (even fractionally)

---

## Tips to Identify Greedy Problem

- Keywords like **“maximize”, “minimize”, “largest”, “smallest”**
- You can sort based on some criteria
- You don’t need to revisit choices once made

---

## Greedy Doesn’t Work For:

- 0/1 Knapsack (DP is better)
- Longest Common Subsequence
- Subset sum problems

  **Always try to prove** if your greedy choice leads to an optimal solution.

If unsure → try solving it using both **Greedy** and **Dynamic Programming**, then compare.

| Feature            | Greedy                                             |
| ------------------ | -------------------------------------------------- |
| Approach           | Local optimal choice                               |
| Time               | Usually efficient                                  |
| Space              | Low                                                |
| When works         | When Greedy Choice Property + Optimal Substructure |
| Not always correct | Must validate with proof or counterexamples        |
