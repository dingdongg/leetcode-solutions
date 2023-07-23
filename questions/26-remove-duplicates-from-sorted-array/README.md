# 26 - Remove Duplicates from Sorted Array

## General Thoughts
- Pretty straightforward, although the question was structured weird.
- There is a "hacky" solution where you could do a linear search through the array, while keeping track of the unique items. Then you just overwrite the input array with these unique numbers (which is still `O(n)` lol)

## Things to note
- Key is to maintain a set of the unique numbers seen so far.
    - If we come across a number that isn't in this set, then we found the unique instance of that number
    - swap this with the leftmost duplicate entry so far
    - add the unique number to the set

### Performance

*Time* - `O(n)` as we iterate the right pointer through the entire `num` array

*Memory* - `O(k)`, as we iterate the left pointer for however many unique numbers there are 

---

## Optimization notes
- Set is overkill for this problem, since the array is sorted already
    - faster way to see if `nums[i]` is a duplicate is to see if `nums[i - 1]` equal to it; if it is, then `nums[i]` is a duplicate
    - we can maintain two pointers: 
        - index to the leftmsot duplicate spot 
        - index to iterate through the array
    - the pointer that keeps track of the next duplicate spot is only incremented `k - 1` times, so it will be equal to the number of unique characters to be returned

### Performance

*Time* - `O(n)` to iterate through the entire array

*Memory* - `O(1)`, just need two pointer variables

---

## Algorithm
```
1. Initialize next duplicate pointer to be 1
2. For i in [1, len(nums)):
    1. if nums[i] != nums[i - 1],
        1. set nums[next_duplicate] to nums[i - 1]
        2. increment next_duplicate by 1
3. return next_duplicate

```
## Things I learned
- Two-pointer technique is like sliding window but has its differences.
    - it's more intuitive to drop the idea of a "window" for two-pointer
    - while sliding window is best for problems related to substrings/subarrays, two-pointer doesn't require this contiguous collection
    - they're similar in the sense that there are "left" and "right" pointers in both, and the left pointer will (in general) never surpass the right pointer

## Things to improve
- I'm not as comfortable with the two-pointer techinque than I thought I was, I assume it's because I'm so used to the sliding window technique at this point. I need more practice with two-pointer questions.