# 76 - Minimum Window Substring

## General Thoughts
- A little more difficult than the previous problem (`567`), but once I figured out the left-sliding condition and the substring comparison mechanism, it was straightforward
- It was easier to solve the problem once I had a solid logic for solving the problem on paper before I started coding at all, instead of trying to debug my solution as I worked through it
- Starting from the brute force solution and optimizing really helped with this problem, as the core mechanism still applied

## Things to note
- for any 2 given substrings `s` and `t`, `s` is a min. window containing all letters in `t` IFF for all characters `i` in `t`, `t_freq[i] <= s_freq[i]`
    - can't do whole hash table comparisons, since the window of `s` may include characters that aren't in `t`; also, we may have more instances of a particular letter in `s` than in `t` (which is still valid)
    - we are able to keep track of which letters have yet to be fully included by using a set
        - pop the letter from the set once we have enough of it
        - as we increment left pointer, add the letter back once we no longer have enough of it

### Performance

*Time* - `O(len(s) + len(t))`

*Memory* - `O(52 * 3) = O(1)`

---

## Optimization notes

### Performance

*Time* - ``

*Memory* - ``

---

## Algorithm
1. Calculate the frequecy table for `t`
2. Calculate the unique letters in `t` (=`incomplete`)
3. Initialize left and right pointers (and minimum pointers to use at the end)
4. While right pointer is not past the end of string `s`,
    1. if `s[r]` is one of the letters in `t`, increment `s_freq[s[r]]`
    2. if `s[r]` is in `incomplete` and `s_freq[s[r]] >= t_freq[s[r]]`,
        1. remove `[s[r]]` from `incomplete`, since it is now complete
        2. While `incomplete` is empty,
            1. update minimum pointers
            2. if `s[l]` is one of the letters in `t` (or `s`, doesn't matter since we only add letters to `s_freq` if it exists in `t_freq`),
                1. decrement `s_freq[s[l]]`
                2. if `s_freq[s[l]] < t_freq[s[l]]`, add `s[l]` to `incomplete`
            3. increment left pointer
    3. increment right pointer
5. If the length from minimum pointers is greater than the length of the string, return `""`
6. Otherwise, return `s[min_ptr.left:min_ptr.right]`

## Things I learned
- With a lot of the problems that span a big search space (ie. all possible substrings), it is helpful to start from the brute force solution to figure out a core mechanism used to solve the problem (in this case, it was deriving the inequality `t_freq[i] <= s_freq[i]`)
- Don't get caught up with the "What-Ifs" for too long, often a waste of time
- Walk through a test case from start to finish **WITHOUT** skipping steps, this can help catch bugs/logical errors