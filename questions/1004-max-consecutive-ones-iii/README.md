# 1004 - Max Consecutive Ones III

## General Thoughts
- Easy. This problem was almost identical to the "maximum substring with at most `k` replaceents" question with a simpler variation on the question, so I noticed the pattern immediately.

## Things to note
- With any sliding window question, brute force is going to be `O(n^2)` runtime, since the number of possible subarrays in an array of length `n` is `O(n^2)`.

### Performance

*Time* - `O(n^2)`

*Memory* - `O(1)`, need just one variable to keep track of the number of zeros in any given subarray

---

## Optimization notes
- This is simpler than the "maximum substring with at most `k` character replacements" question, because the items of the array are binary digits. On top of that, we only need to keep track of the frequency of 0s, because the problem wants to find the maximum number of consecutive 1s we can have by *flipping at most `k` 0s*
    - this means the actual number of 1s in the array doesn't need to be counted; it can always be calculated as `(r - l + 1) - freq[0]`

### Performance

*Time* - `O(n)`

*Memory* - `O(1)`, only need a few variables for the window, max size, and 0 frequency

---

## Algorithm
```
1. Init left and right pointers to 0
2. Init max_size to 0
3. Init zero_freq to 0
4. While the right pointer has not passed the end of the array,
    1. If nums[r] is 0, increment zero_freq
    2. if zero_freq <= k, set max_size to max(max_size, r - l + 1)
    3. while zero_freq > k and (r - l + 1) > max_size,
        1. if nums[l] is 0, decrement zero_freq
        2. increment left pointer by 1
    4. increment right pointer by 1
5. return max_size
```
## Things I learned
- Not much, since I already knew how to solve a more complicated version of the problem

## Things to improve
- Even if the problem seems straightforward and dead simple, resist the urge to jump directly into the code. Always voice your thought process out loud first as these can help catch unexpected edge cases that can be easily overlooked