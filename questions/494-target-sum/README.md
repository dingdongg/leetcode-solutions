# 494 - Target Sum

## General Thoughts
- Coming up with the naive recursive solution wasn't too bad, but not too easy either. Memoizing my recursive solution was where I struggled

## Things to note
- there are a total of `2^n` possible expressions possible, as each item can be prepended with either a "+" or a "-"
- brute force way is to check every one of these possible expressions. If they are equal to are target, we include that expression in our count 

### Performance

*Time* - `O(2^n)`

*Memory* - `O(2^n)`, since a call stack will be initialized for every leaf node in the decision tree 

---

## Optimization notes
- there are a lot of redundant calculations that occur in the decision tree
- by caching/memoizing these calculations, we can prevent repeated calculations in the future and reduce runtime
- in order to use the value of the cache, we must take into consideration the pair `(index, curr_sum)`
    - cache values at different indices won't work, since the trees will have different heights
    - cache values at different curr_sums won't work (obviously)
    - one additional optimization can be done by caching `(index, abs(curr_sum))`
        - the two branches at level 1 are negative mirrors of each other; 
            - if the target `x` occurs `t` times in the left branch and `-x` occurs `t'` times, `x` will occur `t'` times and `-x` `t` times in the right branch
            - by looking for `target` and `-target`, we can disregard almost half of the initial search space (which is still `O(2^n)`, but still - pretty neat imo)

### Performance

*Time* - `O(sum(arr))`, since we the memoized array can alleviates redundant computations; total number of possible sums ranges from `[-sum(arr), sum(arr)]`; (not necessarily every integer in the range, but it gives a good worst-case upper bound)

*Memory* - `O(n)`

---

## Algorithm
```
1. Initialize an empty dictionary as the memo
2. Call solve(nums, start_idx, target, curr_sum) as solve(nums, 0, target, 0)
3. solve():
    1. if the pair (start_idx, curr_sum) exists in the memo, return memo[pair]
    2. if start_idx == len(nums),
        1. return 1 if target == curr_sum; otherwise 0
    3. call solve(nums, start_idx + 1, target, curr_sum + nums[start_idx]) to find positive ways
    4. call solve(nums, start_idx + 1, target, curr_sum - nums[start_idx]) to find negative ways
    5. set memo[pair] to the sum of steps 3.3 and 3.4
    6. return memo[pair]
```
## Things I learned
- DP isn't that complicated
- For DP problems, it helps to first find the recurrence relation for the problem. Write a brute force solution first, and then once you're done try to optimize the runtime by introducing memoization/tabulation
- memoization usually involves a top-down approach, whereas tabulation is a bottom-up approach
    - memoization is useful where you don't necessarily have to compute all subproblems; you can choose to compute only the subproblems that you require
    - tabulation is nice where you have to compute and memoize the solution to almost all subproblems in the search space; this is especially common in Fibonacci problems (`fib(n) = fib(n-1) + fib(n-2)`)

## Things to improve
- LOOK AT THE RECURSION TREE MORE CLOSELY; I completely missed the repeated calculations in my tree, and so I didn't know how to memoize my naive solution