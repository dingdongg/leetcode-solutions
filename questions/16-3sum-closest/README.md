# 16 - 3Sum Closest

## General Thoughts
- Ok. I could tell it was a spin on `15 - 3sum`, so I tweaked the solution for that and arrived at a solution without major issues, although I did run into tiny hiccups

## Things to note
- Similar to 3sum, the brute force solution would be to check every triplet. If `target - sum(triplet)` is smaller than anything we've seen so far, update our `min_so_far`

### Performance

*Time* - `O(n^3)`

*Memory* - `O(1)`

---

## Optimization notes
- Similar to 3sum, we can optimize by utilizing the two sum II solution
    - The problem is basically identical to `15 - 3sum`, but with 2 caveats:
        1. there is now a `target` input (instead of looking for sums of 0)
        2. there is no guarantee that there will be an exact solution (ie. looking for the *closest* possible answer)
- we are looking for a solution, where:
    - the absolute distance between the target and current sum is a **minimum**
    - the two sum II solution helps, because the sum of the triplets will converge to the target value.
        - if the current sum is too big, shift the right pointer down to shrink the sum
        - if the current sum is too small, shift the lefft pointer up to raise the sum
        - if equal, return it.
        - so, we must sort the input array first

### Performance

*Time* - `O(n^2)`, same logic as 3sum. `O(n log n)` to sort, `O(n^2)` b/c we do `O(n)` work over `n` items

*Memory* - `O(1)`, just a few primitive variables for pointer/sum value

---

## Algorithm
```
1. Sort the array
2. Set the closest to a really large integer
3. Set previous to none
4. for n in nums,
    1. if n is equal to the previous number, skip
    2. Initialize l and r pointers to i + 1, len(nums) - 1
    3. while l < r,
        1. compute the sum of the triplets
        2. compute the absolute difference of target - curr_sum
        3. if (result from 4.3.2) < (abs. diff of target - closest),
            1. update closest to be (result from 4.3.2) 
        4. if curr_sum > target, decrement r by 1
        5. else if curr_sum < target , increment l by 1
        6. otherwise, return curr_sum
    4. Set previous to n
5. return closest
```
## Things I learned
- Patterns is the way to learn leetcode. A lot of similar pattern-problems are literal variations of one another, and there are only so many ways to put a twist on a question
- I adapted a previous problem to solve a different problem! (3sum -> 3sum closest)

## Things to improve
- I *knew* this was a variation on 3sum, so I got arrogant and jumped right into coding
    - because of this, I ran into hiccups like:
        - not realizing I had to return the *sum* of the triplets, not the triplet itself
        - returning the minimum *difference* instead of the minimum *sum*
        - subtle logical bugs
    - next time, even if you know the solution, try to write it out on paper first to consolidate your logic to prevent the above hiccups