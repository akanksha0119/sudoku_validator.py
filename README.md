

### ✅ Valid Board Example
```python
Input:
valid_board = [
  [5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9],
]

custom_zones = [[(i, i) for i in range(9)], [(i, 8 - i) for i in range(9)], ...]

Output:
True



## 📋 Sample Test Cases

| Test Case | Description                        | Expected Result |
|-----------|------------------------------------|-----------------|
| Test 1    | Valid board with custom zones      | ✅ Passed        |
| Test 2    | Row violation                      | ✅ Passed        |
| Test 3    | Custom zone violation              | ✅ Passed        |

---

