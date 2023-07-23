# 1 - Two Sum

## General Thoughts
- Easy, solved before.

## Things to note
- Brute force solution would be to check every pair of numbers to see if they add up to `target`

### Performance

*Time* - `O(n^2)` since there are `O(n^2)` pairs

*Memory* - `O(1)` for two pointers

---

## Optimization notes
- Better solution is to store a hash table of `target - n`. As we do a linear search through the array, if we come across an item `= target - n`, we can retrieve the index store in the hash table and return it with the current index

### Performance

*Time* - `O(n)`, one linear search through the array

*Memory* - `O(n)`, hash table stores `O(n)` entries from `nums`

---

## Algorithm
```
1. Initialize a hash table (need)
2. for every item in nums,
    1. if the item is a key in the hash table, return [current index, need[item]]
    2. otherwise, set need[target - item] = current index
3. return [-1, -1] if no solution is found
```
## Things I learned
- n/a

## Things to improve
- n/a