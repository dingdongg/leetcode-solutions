# 424 - Longest Repeating Character Replacement

## Things to note
- For any given substring, it can become a string with only 1 unique letter if it satisfies
  `length - max_freq <= k`, where:
    - `max_freq` is the most frequent character in the substring 
    - `k` is the number of replacements possible
- One of the constraints of this problem is that the string will only ever consist of uppercase English letters (26 letters)
    - this means that a brute force search on a frequency table to calculate `max_freq` is still `O(1)`, albeit slow

### Performance

*Time* - `O(26 * n) = O(n)`

*Memory* - `O(1)`

---

## Optimization notes
- In the equation `length - max_freq <= k`, note that as length increases, `max_freq` must also increase accordingly to satisfy the inequality
    - this means that as we slide the right pointer (increase the length), the only way for us to potentially get a larger value for our `max_length` variable is if `max_freq` also increases accordingly; if it stays the same and/or decreases, the inequality would not be satisfied (thus our `max_length` variable would not be updated)
- this gets rid of the need to re-calculate the `max_freq` whenever we slide our left pointer; we keep it at its current value
    - re-calculating `max_freq` to get a new `max_length` value will not work since the inequality will never be satisfied (since length is decreasing as we slide our left pointer)

### Performance

*Time* - `O(n)`

*Memory* - `O(1)`

---

## Things I learned
- Step back from the problem if feeling stuck, approach at a slightly different angle when you come back
- sliding window is useful for optimization problems, in this case, a maximization problem
- think simple
- If really stuck, logically work through the problem from a brute force solution