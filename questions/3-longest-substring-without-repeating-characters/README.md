# 3 - Longest Substring Without Repeating Characters

## General Thoughts
- Straightforward, I think I am getting the hang of identifying sliding window problems

## Things to note
- Brute force: check each subarray, see if it only has distinct characters
- inefficient because of the duplicate work done 

### Performance

*Time* - `O(n^2)`, since there are `O(n^2)` possible substrings

*Memory* - `O(set(s))`, bounded by the number of unique characters in `s`

---

## Optimization notes
- Can reduce runtime complexity by using sliding window technique
    - substring/subarray condition checks out
- expand the window while we only have 1 instance of each character
- once the above condition is broken, start shrinking from the left to restore it
- at every iteration, update `max_size` to be `max(max_size, r - l + 1)`
- return `max_size`

### Performance

*Time* - `O(n)`; for each item in the array, you only add/remove it to/from the set once each, which is `O(1)`

*Memory* - `O(set(s))`; bounded by the number of unqiue characters in `s`

---

## Algorithm
```
1. Initialize left and right pointers to 0
2. Initialize max_size to 0
3. Initialize an empty set
4. While the right pointer has not passed the end of the string,
    1. while s[r] in the set,
        1. remove s[l] from the set
        2. increment left pointer by 1
    2. update max_size to be max(max_size, r - l + 1)
    3. increment right pointer by 1
5. return max_size
```
## Things I learned
- The condition where we skip looking at potential subarrays whose length `< max_size` doesn't always hold, like this problem

## Things to improve
- Don't take the "sliding window" template for granted; always be conscious of the pieces
of the template and ask yourself, "does it work here?"