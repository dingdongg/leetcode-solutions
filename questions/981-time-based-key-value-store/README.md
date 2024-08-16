# 981 - Time Based Key-Value Store

## General Thoughts
- A lot easier than i initially thought

## Things to note
- binary search is useful, since we have the concept of timestamps with this new data structure
- with the constraint that for every `set(k, v, timestamp)`, `timestamp` will be strictly increasing
    - this means that we can trivially maintain sorted order of our items in a dynamic array by simply appending incoming values (strictly increasing = UINQUE AND INCREASING)
    - with a sorted array of timestamp values, we can perform binary search to get our items in worst case of `O(log n)` time

### Performance

*Time*:
`get(key, timestamp)` - `O(log n)`; worst case occurs when we call `n` `set()` operations all with the same `key`

`set(key, value, timestamp)` - `O(1)`, amortized since we make use of a dynamic array

*Memory* - `O(# of unique (key, timestamp) tuples)`

---

## Algorithm
- very straightforward - check out `main.py`


## Things I learned
- Things that helped:
    - breaking the problem down into manageable/understandable pieces
    - writing down my understanding of the problem requirements
    - noting any useful constraints
    - walking through an example or two to gain more intuition
    - use the examples to derive a general fact about the algorithm (lines 45 and onwards in the notes)
    - utilize all (or some) of the above observations to come up with an implementation plan

## Things to improve
- Using this observation-based method will take some time, more practice is required