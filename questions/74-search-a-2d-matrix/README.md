# 74 - Search a 2D Matrix

## General Thoughts
- easy

## Things to note
- this is just standard binary search applied both "vertically" and "horizontally"
- note that left and right pointers in a binary search will always converge - for this question, 
the question is: *where* in the row do these two pointers converge?
    - if they converge at the left (ie. `l = r = 0`) AND `target != matrix[row][0]`, the target
      may be in one of the previous rows
    - if they converge at the right (ie. `l = r = n`) AND `target != matrix[row][n]`, the target
      may be in one of the next rows
    - if they converge anywhere else within the array AND target isn't found, then the target
      doesn't exist anywhere in the matrix
    - all of the above is possible due to the sorted nature of the matrix
    - thus, if we haven't returned false by now, we perform another binary search to find the 
      appropriate row to search (the next "middle" row)

### Performance

*Time* - `O(log(m) * log(n))` - `log(n)` per row, `log(m)` rows searched in the worst case

*Memory* - `O(1)` just pointer variables used, and this solution is iterative so no use of call stacks

---

## Optimization notes

From the problem statement:

> The first integer of each row is greater than the last integer of the previous row.
>

- This means that it is possible to narrow down the target ROW with one "vertical" binary search,
rather than performing this search every time we fail to find the target in any given row
- So, the runtime complexity will be dictated by 1 binary search through the rows + 1 binary search
through the given row 
- for sufficiently large values of `m` and `n`, this solution should be significantly faster

### Performance

*Time* - `O(log(m) + log(n)) == O(log(mn))` as explained above

*Memory* - `O(1)`, same as the un-optimized version

---

## Algorithm
```
1. Set n = len(matrix[0])
2. Set rl, rh = 0, len(matrix)
3. While rl < rh,
    1. Set rm = (rl + rh) >> 1
    2. if the target is equal to either the first or last item of matrix[rm], return True
    3. if the target is BETWEEN the first and last items of matrix[rm], 
        1. Set rl = rm and break out of loop
    4. else if the target is smaller than the first item of matrix[rm], 
        1. Set rh = rm
    5. else if the target is greater than the last item of matrix[rm],
        1. Set rl = rm + 1
4. if rl >= rh, return False (as this means we couldn't find a candidate row to search)
5. Set cl, ch = 0, n
6. Set row = matrix[rl]
7. While cl < ch,
    1. Set cm = (cl + ch) >> 1
    2. if row[cm] == target, return True
    3. else if row[cm] < target, set cl = cm + 1
    4. else if row[cm] > target, set ch = cm
8. return False
```
## Things I learned
- binary search is probably the easiest of the algorithms to understand 