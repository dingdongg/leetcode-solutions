# 252 - Meeting Rooms

## General Thoughts
- Easy

## Things to note
- Not much. General application of merging intervals.

### Performance

*Time* - `O(n log n)` to sort meeting times by their start times

*Memory* - `O(1)`

---

## Algorithm
```
1. Sort intervals in a non-decreasing order, based on the intervals' start times
2. For i from 1..len(intervals),
    1. If intervals[i].start < intervals[i - 1].end, return False
3. Return True
```
## Things I learned
- Not much for this question

## Things to improve
- n/a