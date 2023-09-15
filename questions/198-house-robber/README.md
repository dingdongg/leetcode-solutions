# 198 - House Robber

## General Thoughts
- Straightforward, it's a classic fibonnaci DP problem at this point

## Things to note
- At every house `i`, you ahve 2 choices:
    1. rob `i` and go to `i + 2`
    2. don't rob `i` and go to `i + 1`
- between these choices, we want the choice that *maximizes* the money we steal
- since we have 2 choices at each house, we have `O(2^n)` possible stealing combinations
### Performance

*Time* - `O(2^n)`, number of nodes in the solution tree

*Memory* - `O(2^n)`, one call stack initialized for every node in the tree

---

## Optimization notes
- Some subtrees occur more than once in the whole solution tree
- by memoizing our computations, we only compute results once and avoid redundant and expensive calculations

### Performance

*Time* - `O(n)`, cost of every stealing every house in the array is computed once

*Memory* - `O(n)`, memoized table size is proportional to `n`

---

## Algorithm
```
1. Initialize empty memo table
2. Set nums as a global array
3. return solve(0)
4. solve(start_idx):
    1. if start_idx == len(nums), return 0
    2. if start_idx + 2 is not cached, set memo[start_idx + 2] to solve(start_idx + 2)
    3. if start_idx + 1 is not cached, set memo[start_idx + 1] to solve(start_idx + 1)
    4. set memo[start_idx] to max(nums[start_idx] + memo[start_idx + 2], memo[start_idx + 1])
    5. return memo[start_idx]
```
## Things I learned
- Fibonacci DP problems all share a verty similar structure, with minor differences in the constraints involved