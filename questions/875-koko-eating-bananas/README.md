# 875 - Koko Eating Bananas

## General Thoughts
- I struggled way too hard considering the difficulty of this problem

## Things to note
- `k` is bound by `[1, max(piles)]`
- thus, we can employ binary search on the search space of `k` and find the minimum value of `k`
such that we can eat all bananas in all piles in `<= h` hours at a rate of `k` per hour

### Performance

*Time* - `O(log(max(p)) * p)`, `O(p)` to find the max pile count and `log(max(p))` to do binary search

*Memory* - `O(1)`

---

## Algorithm
```
1. if h == length of piles, return max(piles)
2. set slowest, fastest = 1, max(piles) + 1 (+1 is done to avoid off-by-one errors)
3. set res = fastest
4. while slowest < fastest,
    1. set bph = (slowest + fastest) >> 1
    2. set time_taken = 0
    3. for p in piles,
        1. time_taken += ceiling of (p / bph)
    4. if time_taken <= h,
        1. set fastest = bph
        2. res = min(res, bph)
    5. otherwise if time_taken > h,
        1. slowest = bph + 1
5. return res
```
## Things to improve
- I have to learn how to NOT overthink the problem from the get-go
- Avoid "premature optimizations" at all costs. Just always try to stick to brute force solution first,
then evolve your solution after you have the brute force solution working.
- the reason I was stuck on this problem was because I tried to make optimizations that were way too
difficult to execute on the first try (not sure if such an optimization was even possible)