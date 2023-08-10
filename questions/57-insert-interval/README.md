# 57 - Insert Interval

## General Thoughts
- Pretty easy, although there were some edge cases that I didn't consider in my initial solution

## Things to note
- The input is already sorted, so we can apply a similar approach to problem `#56`
- At a high level, there are 2 main cases: 
    1. The new interval **overlaps** with existing interval(s)
        - In this case, the intervals that overlap with the new interval are all merged into 1 interval
    2. The new interval **does not overlap** with any existing interval
        - There are 3 types:
            a. new interval goes at the beginning of the intervals list
            b. new interval goes somewhere in between the existing intervals
            c. new interval goes at the end of the intervals list
        - As we iterate through the list, we can keep track of the index where the index should be stored
            - for every interval that we find goes *before* the new interval, increment index by 1
        - If we find that no merging occurred (ie. no overlaps), we can use this index to properly insert our new interval into the list

### Performance

*Time* - `O(n)`, there is no sorting and we do a linear scan through the list. There is some list slicing involved but that is still `O(n)`

*Memory* - `O(n)`, to build up the return list

---

## Algorithm
```
1. Init an empty return list (ret)
2. Init i and insert_pos to 0
3. While i < len(intervals),
    1. If the current's end is less than new's start, or current's start is greater than new's end,
        1. Append current interval to ret
        2. if current's end is less than new's start, increment insert_pos by 1
        3. Increment i by 1
    2. Otherwise, 
        1. Set merged to be a new interval with start = min(curr's start, new's start) and end = new's end
        2. While i < len(intervals) and intervals[i]'s start <= new's end,
            1. Set merged's end to max(merged's end, intervals[i]'s end)
            2. Increment i by 1
        3. Append merged to ret
        4. return ret + intervals[i:]
4. Return ret[0:insert_pos] + [newInterval] + ret[insert_pos:]
```
## Things I learned
- It seems like merging intervals isn't so hard, hopefully that is the case for other variations of these problems
- These patterns (merging intervals, linked list, 2-pointer, sliding window) all build on top of fundamental data structures (array, hash tables, sets seem to be the most common ones)

## Things to improve
- I didn't fully sit down to consider all possible cases before writing the code, which meant a lot of back and forths between submitting-debugging-submitting.
    - **SOLUTION: DON'T MOVE TO CODING UP THE SOLUTION TOO FAST, STOP AND CHECK IF YOU HAVE CONSIDERED ALL EDGE CASES**