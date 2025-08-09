### Problem Statement

You are selling lemonade for $5 per cup. Customers line up to buy lemonade and each pays with either a **$5, $10, or $20** bill.

You must provide **correct change** for each customer **in the order they appear**, using only the bills you have collected from previous customers. You start with **no change**.

Determine if you can provide the correct change to every customer in line.

Return `true` if it is possible to do so for every customer; otherwise, return `false`.

### Input

- `bills`: an integer array where `bills[i]` is the bill the i-th customer pays (`5`, `10`, or `20`).

### Output

- `true` if you can give the correct change to every customer.
- `false` otherwise.

---

### Greedy Strategy

Keep track of how many **$5 bills** and **$10 bills** you have at any point.

For each bill in the `bills` array:

- If it's `$5`: no change is needed. Increment your $5 bill count.
- If it's `$10`: give back one $5 as change. If not available, return `false`.
- If it's `$20`: try to give one $10 + one $5 as change (preferred), else try three $5s. If neither is possible, return `false`.

---

### Algorithm

```python
def lemonade_change(bills):
    five, ten = 0, 0

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:  # bill == 20
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

    return True

```

---

### Example 1

```
Input: bills = [5, 5, 10, 5, 20]
Output: true

Explanation:
- $5: keep it
- $5: keep it (now have 2 fives)
- $10: give 1 five (now 1 five, 1 ten)
- $5: keep it (now 2 fives, 1 ten)
- $20: give 1 ten + 1 five (now 1 five)
All customers received correct change.

```

---

### Example 2

```
Input: bills = [5, 5, 10, 10, 20]
Output: false

Explanation:
- After serving four customers, you have two tens, zero fives.
- Fifth customer pays with $20; you cannot return $15 change.

```

---

### Example 3

```
Input: bills = [5, 5, 10, 20]
Output: true

```

---

### Time and Space Complexity

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |
