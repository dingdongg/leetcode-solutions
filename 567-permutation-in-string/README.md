# 567 - Permutation In String

## General Thoughts
- Was pretty straightforward once I found that all permutations have same letter frequency

## Things to note
- The condition to start shrinking window from the left is when your window exceeds `len(s1)`, since that means that it is no longer a permutation of `s1` (extra letter is included)
- Optimizing the hash table comparisons can *maybe* be optimized (although `O(1)`, it suffers the same problem as the frequency table comparison in `../424/`)

### Performance

*Time* - `O(1)`

*Memory* - `O(1)` -> 2 dicts of max size 26 and 2 pointers

---

## Algorithm
1. Populate the frequency table of characters in `s1`
2. Initialize left and right pointers to 0
3. While right pointer is not at the end of `s2`, do the following:
    1. increment s2 frequency table at `s2[r]`
    2. if length `(r - l + 1) > len(s1)`, shrink left window and decrement `s2[l]`; increment l
    3. if `s1` freq table equals the `s2` freq table, return `True`
    4. increment r
4. return `False`

## Things I learned
- A common pattern in sliding window techniques is expanding the right window until some condition is broken, at which point you shrink the left window until it is satisfied again
- Work out a solid no-code solution *ON PAPER* before coding