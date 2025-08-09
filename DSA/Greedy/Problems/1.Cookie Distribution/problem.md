### Problem Statement

A teacher wants to distribute cookies to students such that:

- Each student gets **at most one cookie**.
- Each student has a **minimum size requirement** for the cookie they'll accept.
- A cookie can only be given to a student if its size is **greater than or equal to** the student’s requirement.

Your goal is to **maximize the number of students** who can receive cookies.

### Input

- `students`: an array where `students[i]` is the minimum cookie size required by the i-th student.
- `cookies`: an array where `cookies[j]` is the size of the j-th cookie.

---

### Output

- Return the **maximum number of students** that can be satisfied.

---

### 🧠 Greedy Approach

1. **Sort both arrays** – students by requirement, cookies by size.
2. Use two pointers:
   - One for the `students` array (`i`)
   - One for the `cookies` array (`j`)
3. Try to assign the **smallest suitable cookie** to each student.
4. If the cookie size is sufficient (i.e., `cookies[j] >= students[i]`), assign it and move both pointers.
5. Otherwise, skip to the next cookie (`j++`).

---

### Example 1

```
Input: students = [1, 2, 3], cookies = [1, 1]
Output: 1

Explanation:
Only one student (with need 1) can be satisfied with a size-1 cookie.

```

---

### Example 2

```
Input: students = [1, 2], cookies = [1, 2, 3]
Output: 2

Explanation:
All students can be satisfied as cookies are large enough.

```

---

### Example 3

```
Input: students = [4, 5, 1], cookies = [6, 4, 2]
Output: 3

Explanation:
All three students can be satisfied by appropriate cookie assignment.

```

### Time and Space Complexity

| Metric | Value                              |
| ------ | ---------------------------------- |
| Time   | O(n log n + m log m) — for sorting |
| Space  | O(1) — constant extra space        |
