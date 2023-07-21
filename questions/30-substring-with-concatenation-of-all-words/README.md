# 30 - Substring with Concatenation of All Words

## General Thoughts
- Pretty hard. I thought I had most of the logic down but there was a pretty major set of cases that I overlooked. Tried implementing an optimal solution around this but couldn't think of one, so I resorted to a sort of brute force workaround.

## Things to note
- The basic premise is sliding window technique, since we are looking for substrings.
- All permutations share the exact same frequency of letters
    - but, the added complexity to this question is that each `word` is considered a `letter`
    - ie. for `["foo", "bar"]`, `"foobar"` is valid but not `fbaoor`
    - to solve this issue, I also considered the frequency of each *word* from `words` that occurred in any given substring
        - I did this by doing a basic linear search through the substring and counting up the words in chunks of `word_leng`, then comparing the word frequency tables
        - this is the "brute force" part of the solution, and I don't like it. There is probably a way to optimize this that I overlooked

### Performance

*Time* - `O(len(s) * O(len(words)))`, since you're doing `O(len(words))` work for every substring of length `concat_string_leng`, of which there are `O(len(s))`

*Memory* - `O(len(s))` since in the worst case, every index of `s` may be stored

---

## Optimization notes
- TODO

### Performance

*Time* - ``

*Memory* - ``

---

## Algorithm
```
1. 
```
## Things I learned
- Difficult question, and although my solution isn't great I managed to solve it in the end
- My logical path to the solution was pretty good

## Things to improve
- Get better at coming up with solutions to optimize inefficient parts of my code
    - in this instance, coming up with a faster way to see if a substring is a *valid* concatenated string of items in `words`