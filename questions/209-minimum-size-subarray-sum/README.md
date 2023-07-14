# 209 - Minimum Size Subarray Sum

## General Thoughts
- Very straight forward. I think I am starting to get what people mean when they say to
spot the patterns, and apply the correct technique for that problem's pattern
- Solved in < 30 minutes YAY

## Things to note
- Naive solution is to compute every possible subarray, starting from the smallest subarrays possible. When we come across a subarray whose sum is `<= target`, update 
the length of the smallest subarray size seen so far
- at the end, return the smallest subarray size value

### Performance

*Time* - `O(n^2)` since the number of total subarrays for an array of length `n` is on the order of `n^2`

*Memory* - `O(1)` since we only need to keep track of the current sum and the minimum sum

---

## Optimization notes
- There is a lot of duplicate work done in the brute force method; you have to re-compute the sum for subarrays that start at any index `i`
    - this leads to the `O(n^2)` time complexity since you are doing `O(n)` work at each index
    - if we can keep the operations done at each index at `O(1)`, we can achieve `O(n)` runtime
- since the array only consists of positive integers, expanding any subarray will increase its sum
    - and correspondingly, shrinking size of window will decrease its sum
- what we can do is to try and expand just until we reach a sum such that it is `>= target`, and then try shrinking it from the other side until we're back at a point where our sum is `< target`
    - on each iteration where this is true, update our minimum window to be the size of the smaller window seen so far
    - we can keep track of the sum in constant time by adding/subtracting from a `curr_sum` variable

### Performance

*Time* - `O(n)` since we add and subtract each element from `curr_sum`, which is 2 `O(1)` operations per element

*Memory* - `O(1)`, only keeps track of an integer `curr_sum`, `min_size_so_far` and l/r pointers

---

## Algorithm
```
1. Initialize left and right pointers to 0
2. Initialize current sum to 0
3. Initialize minimum window size to len(nums) + 1
4. While the right pointer is not past the array,
    1. increment curr_sum by nums[r]
    2. while curr_sum >= target,
        1. update minimum window size to be min(minimum window size, r - l + 1)
        2. decrement curr_sum by nums[l]
        3. increment l by 1
    3. increment r by 1
5. if minimum window size is len(nums) + 1, return 0; otherwise return the window size
```
## Things I learned
- Sliding window technique is very useful for a lot of problems that involve subarrays/values that correspond to a continuous piece of collection
    - Also helps to cut down the search time dramatically 
- Pacing myself also helps improve focus while I work through a question. I think ~30 minutes is a good timeframe (not too short, not too long)
- Don't overthink questions, often times they are really simple 

## Things to improve
- My solution doesn't translate over completely into code. This is probably because I either:
    1. am not confident with my algorithm at that point, or 
    2. going too fast. It is okay (I THINK??) to take it a little slower when writing up the code solution