# 18 - 4Sum

## General Thoughts
- A lot easier than I initally thought it would be, turns out it was just an extended application of the 3sum algorithm (which, in turn, is based on the sorted 2sum algorithm)

## Things to note
- Brute force solution would be to have 4 nested loops, resulting in `O(n^4)` time

### Performance

*Time* - `O(n^4)`

*Memory* - `O(1)` (excluding the returning list)

---

## Optimization notes
- If you apply the 3sum algorithm which is `O(n^2)`, the runtime can be brought down to `O(n^3)` time
- Principle is the same as 3sum: for every item `n` in the list, compute the triplet that adds up to `target - n`
- Requires sorting since 3sum requires sorting

### Performance

*Time* - `O(n^3)`

*Memory* - `O(1)` (excluding the returning list)

---

## Algorithm
```
1. Sort the list in ascending order
2. Initalize an empty return list
3. Set the previous number to None
4. for every item in the list,
    1. if this item is equal to the previous, skip this iteration
    2. get the triplets that add up to (target - n) using 3sum algorithm
    3. for every triplet found, append n to the triplet and add it to the return list
    4. set prev to be the current item n
5. return return list
```
## Things I learned
- This problem was very derivative of the rest of the "k-sum" series questions. This type of problem could legitimately be extended to any finite number `k` which sounds pretty useful
- This problem doesn't directly make use of the 2-pointer method itself, since it is the sorted 2sum algorithm that makes use of this

## Things to improve
- I immediately noticed the relationship between this question and 3sum/2sum, so I skipped almost instantly to just coding. I should still walk through an example and gain an intuition for the problem (regardless of how derivative the question seems of a related question)