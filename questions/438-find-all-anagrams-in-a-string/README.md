# 438 - Find All Anagrams in a String

## General Thoughts
- Easy. I think it was a mix of the question being pretty easy and me getting more and more familiar with sliding window patterns

## Things to note
- By keeping the window size at length `len(p)`, whenever you encounter an anagram you just append `l` to the return array

### Performance

*Time* - `O(len(s) + len(p))`, since you are doing a constant number of `O(1)` operations per each character in string `s`. You also have to run through `p` to get its frequency table populated

*Memory* - `O(len(s))`, since it is possilbe that the return array holds up to `len(s) - 1` entries

---

## Algorithm
```
1. Init l, r = 0, 0
2. Init s_freq, p_freq to empty dictionaries
3. Init ret to empty array
4. For every letter c in p, increment p_freq[c] by 1
5. While r has not passed the end of the string s,
    1. increment s_freq[s[r]] by 1
    2. if s_freq == p_freq, push l to ret
    3. while (r - l + 1) >= len(p),
        1. decrement s_freq[s[l]]
        2. if s_freq[s[l]] is 0, delete key-value pair from s_freq
        3. increment l by 1
    4. increment r by 1
6. return ret
```
## Things I learned
- The patterns where sliding window technique can be applied is becoming more apparent now

## Things to improve
- Never skip over even a simple overview of the brute force solution, at least for sliding window problems. There is a lot of insight to gain from them that can be re-used in the optimized version of the solution