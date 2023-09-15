# 746 - Min Cost Climbing Stairs

## General Thoughts
- Pretty straightforward, got tripped up by trying to implement memoization into the solution. Eventually managed to figure it out

## Things to note
- At each item in the array, you have two choices: a) walk up one item, or b) walk up two items
    - compute the minimum count from these choices recursively, and add the cost of the current item to the min.
- that gives a branching factor of 2, so the recursive solution produces a binary tree (`O(2^n)` nodes)

### Performance

*Time* - `O(2^n)`, branching factor of 2; exploring the whole tree means looking at all `O(2^n)` nodes

*Memory* - `O(2^n)`, as the solution is recursive. One call stack will be initialized per node in the solution tree

---

## Optimization notes
- Memoizing intermediate results can help reduce the performance complexity
- If the result for walking up one item hasn't been cached, compute it and cache it
- If the result for walking up two items hasn't been cached, compute it and cache it
- Add the current cost to the minimum of the two cached values, and set that to the current index's cache
- this will ensure min. cost of every item in the tree will only ever be calculated once

### Performance

*Time* - `O(n)`

*Memory* - `O(n)` for the memoized table; one entry per item in list

---

## Algorithm
```
1. Initialize an empty memo table
2. Call solve(0, costs) and solve(1, costs) and return the minimum of the two
3. solve(start_idx, costs):
    1. if start_idx >= len(costs), return 0
    2. if start_idx + 1 is not cached, set memo[start_idx + 1] to solve(start_idx + 1, costs)
    3. if start_idx + 2 is not cached, set memo[start_idx + 2] to solve(start_idx + 2, costs)
    4. set memo[start_idx] to costs[start_idx] + min(memo[start_idx + 1], memo[start_idx + 2])
    5. return memo[start_idx]
```
## Things I learned
- It is dead simple to see where DP can be introduced when you first go for a recursive solution
    - **BUT** it is important to recognize the types of suitable problems (= recursive problems with overlapping subproblems)

## Things to improve
- Still not sure of the differences between memoization vs tabulation