# 167 - Two Sum II - Input Array Is Sorted

## General Thoughts
- Straightforward. I'm not sure if it was because I solved this immediately after trying to solve 3sum (which uses 2sum II), or if the question itself was easy.

## Things to note
- The OG solution to two sum uses a hash table. This is because in that problem, the input array is *unsorted*. But, the input here is sorted so we can take advantage of the inherent ordering that exists
- for any given pair of numbers `a` and `b`, when you add them up, you will get a sum `c`. If `c` is `> target`, we need to choose a new set of numbers that takes us closer to the target.
    - This can be done by *shrinking* the sum `c`, which can only be done by moving the left pointer up
    - Similarly, if the sum `c` is `< target`, the only move is to decrement the right pointer
    - since a solution is guaranteed to exist for two sum II, this will always yield an output

### Performance

*Time* - `O(n)` as this uses the two-pointer technique

*Memory* - `O(1)` for the two pointers and intermediate `sum` variable

---

## Algorithm
```
1. Initialize left and right pointers
2. while l < r,
    1. set sum to nums[l] + nums[r]
    2. if sum > target, shrink sum by decrementing r
    3. else if sum < target, increase sum by incrementing l
    4. otherwise, return [l + 1, r + 1]
```
## Things I learned
- I came to this problem after failing to solve 3sum. I learned that complex problems like 3sum is built on this similar, yet simpler problem

## Things to improve
- I need more exposure to two-pointer problems so that I can apply the patterns found in other problems' solutions to harder problems