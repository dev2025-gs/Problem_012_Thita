# Happy Number

## 🧠 Problem Description

Write an algorithm to determine if a number `n` is a **happy number**.
(https://thita.ai/problems/happy-number)

A **happy number** is defined by the following process:

1. Start with any positive integer.
2. Replace the number with the **sum of the squares of its digits**.
3. Repeat the process until:
   - The number becomes `1` (where it will stay), **or**
   - The process enters a cycle that does **not** include `1`.

If the process ends in `1`, the number is **happy**.  
If it loops endlessly without reaching `1`, the number is **not happy**.

Return `true` if `n` is a happy number, and `false` otherwise.

---

## 📌 Examples

### Example 1

**Input:**
n = 19


**Process:**
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1


**Output:**
true


---

### Example 2

**Input:**
n = 2


**Output:**
false


---

## 🔒 Constraints

- `1 <= n <= 2³¹ - 1`

---

## 💡 Approach Overview

- Extract each digit of the number.
- Compute the sum of the squares of its digits.
- Repeat the process.
- Detect whether:
  - The number becomes `1` (happy number), or
  - The number enters a repeating cycle (not a happy number).

Cycle detection can be handled by:
- Storing previously seen numbers in a set, or
- Using Floyd’s Cycle Detection (fast and slow pointers).

---

## 🚀 Summary

A happy number eventually reduces to `1` after repeatedly replacing the number with the sum of the squares of its digits.  
If it never reaches `1` and instead falls into a loop, it is not a happy number.
