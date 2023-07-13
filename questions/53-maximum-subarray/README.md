# 53 - Maximum Subarray

## General Thoughts
- Pretty straightforward. I tried not to focus on the "sliding window" part and moreso
on the problem itself and I arrived at an efficient answer pretty quickly

## Things to note
- Because we are looking for the maximum *subarray*, the elements we look at must be contiguous. If we choose not to include an element at index `i`, we cannot consider the
element at index `i + 1` in our subarray
- Simplest way is to compute all possible subarrays/sums and keep track of the maximum sum to return at the end

### Performance

*Time* - `O(n^2)`, since there are `O(n^2)` possible subarrays

*Memory* - `O(1)`,  no additional lists required since we're only interested in the summed value

---

## Optimization notes
- If we want to solve this in linear time, we should only operate on each element a *constant* number of times, not `n` times
    - at iteration `i` we must *always* include element at index `i` in our sum. As noted above, because we're looking for subarrays, as we iterate through the list 
    we have to include element at index `i`
        - this is simply because, at iteration `i`, we don't know what is stored beyond index `i`. So, in a sense we are being greedy by choosing to expand our subarray
        in hopes of finding an even bigger maximum sum subarray
        - having to always include index `i` means there are only 2 choices at each iteration:
            1. our new sum is the new element at index `i`, OR
            2. our new sum is the sum of the previous sum + new element at index `i`
        - we can compute both in `O(1)` time, so we can just take the maximum of the two and record it as our maximum sum seen so far
            - #1 will be the case if the current sum so far is negative and our new element alone is greater than the current sum alone
                - this is equivalent to sliding the left pointer to index `i`
            - #2 is equivalent to sliding the right pointer by 1
        - the sum here is sort of like the sliding window. At any given point, our sum `s` is the summation of all of the numbers in a particular window!
            - it's a little different than most sliding window techniques, since we don't actually utilize any left/right pointers (although you could, it would be a little more work to do it that way)

### Performance

*Time* - `O(n)`, given the current window `curr_sum`, we only add and subtract elements to `curr_sum` at most once each

*Memory* - `O(1)`, only requires a constant number of integer variables to keep track of

---

## Algorithm
```
1. Initialize max_sum and curr_sum to be the first element of the list
2. for indices 1..n-1:
    1. update curr_sum to be max(curr_sum, curr_sum + nums[i])
    2. update max_sum to be max(max_sum, curr_sum)
3. return max_sum
```
## Things I learned
- The optimized algorithm is formally known as *Kadane's algorithm*, a form of DP
- Sliding window technique was useful here, because the nature of the problem required
us to look at contiguous elements, which is easily done using l/r pointers (or in this case, the entire sum of the window)