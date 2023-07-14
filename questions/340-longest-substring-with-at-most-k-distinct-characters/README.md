# 340 - Longest Substring with At Most K Distinct Characters

## General Thoughts
- Very straightforward, the "longest subarray" part gave it away that the sliding window technique would be useful
- Starting with an example of a brute force solution for these types of problems always help

## Things to note
- Simplest way to calculate this would be to check all subarrays possible 
- One minor optimization you can make is, when you find a substring of length `m` that has at most `k` unique characters, you can stop looking further and start at `k + 1` substrings. Even then, you might end up doing `O(n)` work for `i in [1..n]` which is still bad.
    - example: "abcdefghhhhhhhhhhh", k = 7; for substrings of length 8 and up there is a lot of redundant work being done

### Performance

*Time* - `O(n^2)` since there are `n` possible substring lengths and you are doing `O(n)` work for each substring length

*Memory* - `O(n)` since we're storing up to the entire string

---

## Optimization notes
- We can optimize by reducing down to `O(1)` work per substring length, which would cut runtime down to `O(n)` -> sliding window technique!
- Keep incrementing right pointer while `# unique characters <= k`
    - Once this condition is broken, start incrementing left pointer to restore this condition
- Minor additional optimization #1: as you shrink the window by incrementing the left pointer, you can stop doing so once your window becomes a size equal to `curr_max_size`
    - since we're looking for the longest substring possible, there is no point in looking at substrings smaller than `curr_max_size`
- Minor additional optimization #2: in the problem, there is no constraint on what characters can be included in the string. Calculating the # of unique characters could be done via `len(freq.keys())`, but this can become a bloated constant operation.
    - to alleviate this, keep track of a separate `count` variable. As you add characters into the frequency table that weren't in it previously, increment `count`. And, as you shrink the window from the left, once a character's frequency becomes 0, decrement `count`. Now there is no need to invoke `len(freq.keys())`

### Performance

*Time* - `O(n)`; we are using each letter in the string to increment/decrement our frequency table which is `O(1)` for `n` characters

*Memory* - `O(n)`; you can have at most `n` unique characters, which fills up `n` entries in the frequency table

---

## Algorithm
```
1. Initialize l/r pointers to 0
2. Initialize max_size and distinct_count to 0
3. Initialize an empty frequency table
4. While the right pointer is not past the end of the string:
    1. if s[r] is not in the frequency table, increment distinct_count by 1
    2. increment freq[s[r]] by 1
    3. if distinct_count <= k, set max_size to max(max_size, r - l + 1)
    4. while distinct_count > k and (r - l + 1) > max_size:
        1. decrement freq[s[l]] by 1
        2. if freq[s[l]] is now 0, decrement distinct_count by 1
        3. increment left pointer
    5. increment right pointer
5. return max_size
```
## Things I learned
- I think I am getting good at recognizing sliding window problems: any problem that works with optimizing for a min/max property of a contiguous piece of collection (strings, arrays, etc) 

## Things to improve
- Can't think of much here, didn't run into any major issues