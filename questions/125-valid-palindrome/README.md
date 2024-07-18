# 125 - Valid Palindrome

## General Thoughts
- Easy

## Things to note
- see `main.py` for details; utilized the two-pointer method

### Performance

*Time* - `O(n)`

*Memory* - `O(1)`, just a couple variables for pointers

---

## Algorithm
```
1. set l, r = 0, len(s) - 1
2. while l < r,
    1. while l < r and s[l] is not alpha-numeric, increment l by 1
    2. while l < r and s[r] is not alpha-numeric, decrement r by 1
    3. if l >= r break out of loop
    4. set left, right = s[l], s[r]
    5. if s[l] is an alphabet and s[r] is an alphabet,
        1. if Unicode code point of s[l] < Unicode code point of 'a', set left to its uppercase version
        2. if Unicode code point of s[r] < Unicode code point of 'a', set right to its uppercase version
    6. if left != right, return False
    7. increment/decrement l/r by 1, respectively
3. return True
```