# 15 - 3Sum

## General Thoughts
- Pretty hard. Neetcode came in clutch to show me `167 - Two Sum II`, a problem that 3sum builds upon, which I did not solve before this problem. After I solved `167` it was pretty straightforward.

## Things to note
- The Brute force method would be to check all triplets and see their sums - this is a naive `O(n^3)` solution

### Performance

*Time* - `O(n^3)`

*Memory* - `O(1)` (excluding the return array) for three pointers

---

## Optimization notes
- This can be optimized by transforming the problem to be able to apply the solution for 2sum II.
    - This requires a sorted input, so we must sort this input array
    - Two sum II takes advantage of the fact that the array is sorted, which helps us track down a pair of numbers that add up to a target sum
        - see `167 Two Sum II` for details
    - By choosing the target sum to be the negative reciprocal of one of the numbers in the array (start from the left), we apply the 2sum II solution to the rest of the array to find the triplets that sum to 0

### Performance

*Time* - `O(n^2)`, achieved from sorting (`O(n log n)`) and two sum II (`O(n)`, for `n` iterations)

*Memory* - `Ω(n)`, seems like python3's implementation of sort takes `Ω(n)` memory 

---

## Algorithm
```
1. Sort input array
2. Initialize an empty return array
3. Set previous to be None
4. for every item n in nums,
    1. if n is equal to the previous number, skip it
    2. Initialize left and right pointers to i + 1, len(nums) - 1
    3. While l < r,
        1. set curSum to nums[l] + nums[r]
        2. if curSum > target, decrement r by 1
        3. else if curSum < target, increment l by 1
        4. otherwise,
            1. append the triplet to the return array
            2*. increment l by 1
            3*. while nums[l] == nums[l - 1] and l < r, increment l by 1
    4. set previous to n
5. return return array
```
- *in `4.3.4.2~3`, the same can be achieved by looping while decrementing r by 1 each iteration
    - This is because, for any given pair of numbers `x` and `y`, each integer can only map to one other integer that achieves the same target sum
    - If the sum becomes too big/small, steps `4.3.2~3` decrements/increments `r`/`l` accordingly
    - Thus, it doesn't matter whether you choose to increment/decrement `l`/`r`
## Things I learned
- From what I have seen so far, two-pointer technique involves manipulating two pointers from either ends of a collection (string, list, etc) to optimize a polynomial runtime >= 2
    - in this case, we went from `n^3` to `n^2`

## Things to improve
- I got caught up in my feint memory of solving this problem. My memory did not serve me right since I went in a slightly offset direction which made me stuck
- I skimmed over the brute force solutions. Looking back, if I took the time to dissect the patterns from brute force, I may have been able to solve this problem much more easily
    - next time, do not glance over brute force solutions, do a solid run through at least one example. (like sliding windows!) 