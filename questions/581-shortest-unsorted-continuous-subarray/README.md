# 581 - Shortest Unsorted Continuous Subarray

## General Thoughts
- Hard, I was overthinking the solution again.

## Things to note
- We need to find the anomalies closest to either ends of the array, since both of these anomalies must be included within the sort (and thus will dictate the minimum subarray size required)
- as we iterate from left to right, the last element involved in a falling slope will mark where our subarray will end
- as we iterate from right to left, the last element involved in a rising slope will mark where our subarray will start
- then you can take the difference between the start/end indexes to get result

### Performance

*Time* - `O(n)`, 2 `O(n)` scans through the array

*Memory* - `O(1)`, just a few constant variables required

---

## Algorithm
```
1. Initialize max_so_far and min_so_far to be the first and last items of the list, respectively
2. Initialize start and end indexes to -1
3. For every item n from left to right,
    1. if n < max_so_far, set end pointer to current index
    2. set max_so_far = max(max_so_far, n)
4. For every item n from right to left,
    1. if n > min_so_far, set start pointer to current index
    2. set min_so_so_far = min(min_so_far, n)
5. if start pointer isn't -1, return (end - start + 1)
6. otherwise, return 0
```
## Things I learned
- I shouldn't be bound to this idea that I can only iterate through the array once; one of the solutions on LC loops through the array 4 times and still achieves `O(n)` time

## Things to improve
- Got caught up with minute details again...
    - I should start the problem off by thinking of a dead simple solution
    - Will still require analysis of the problem domain, but will still help getting started