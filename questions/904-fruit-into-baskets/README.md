# 904 - Fruit Into Baskets

## General Thoughts
- Straightforward. Noticed that it boiled down to a "max continuous subarray" question, which prompted for sliding window

## Things to note
- Brute force: you could compute all possible subarrays and check the # unique numbers in the subarray
- inefficient since you are doing a lot of duplicate work (`O(n)` work for every subarray length)

### Performance

*Time* - `O(n^2)`, since you are doing `O(n)` work for each subarray length possible

*Memory* - `O(n)`, since you have to manage a set of integers seen in the subarray

---

## Optimization notes
- Generic sliding window problem
- Expand the window as much as you can while satisfying the condition that there are at most 2 unique integers in the window
- Once you break this condition, start shrinking the window from the left until this condition is restored

### Performance

*Time* - `O(n)`, you are doing `O(1)` per item (incrementing/decrementing freq. table, updating `max_size`, etc.)

*Memory* - `O(n)`, since there are `O(n)` possible unique numbers in `fruits`

---

## Algorithm
```
1. Initialize left and right pointers to 0
2. Initialize max_size and count to 0
3. Initialize an empty hash table
4. While the right pointer has not passed the end of the array,
    1. if freq[fruits[r]] == 0, increment count by 1
    2. increment freq[fruits[r]] by 1
    3. if count <= 2, set max_size to max(max_size, r - l + 1)
    4. while count > 2 and (r - l + 1) > max_size:
        1. decrement freq[fruits[l]] by 1
        2. if freq[fruits[l]] == 0, decrement count by 1
        3. increment left pointer by 1
    5. increment right pointer by 1
```
## Things I learned
- For problems in foreign domains, it's important that I translate them into the programming domain
    - Picking fruits from trees => find length of max. subarray
- Once you make this translation, try to identify the pattern and apply appropriate data structures/algorithms to solve the problem

## Things to improve
- Need to articulate my thought process better (ie. less stuttering). Helps to speak out loud as I work through the problems to simulate a real technical interview