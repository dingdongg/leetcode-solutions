# 759 - Employee Free Time

## General Thoughts
- Surprisingly easy question for an LC hard

## Things to note
- Common free times are the "gaps" in the employees' schedules
    - there are no intervals occurring within that time interval
    - this interval is defined as `[e, s]` where `e` is the end time of the last interval and `s` is the start time of the first interval after the free time
    - we can keep a count of the total number of "occupied" employees at any given point in time. When this counter hits 0, we know that all employees are free, so we mark that timeframe as free
    -  we need to lists `starts` and `ends` to keep track of all start/end times in sorted order

### Performance

*Time* - `O(n log n)`, requires sorting of employee start/end times into two lists

*Memory* - `O(n)`, two lists to hold all employee start/end times

---

## Algorithm
```
1. Init two empty lists `starts` and `ends`
2. For every employee in schedule,
    1. For every second i in 1..len(employee),
        1. Append employee[i - 1] to starts
        2. Append employee[i] to ends
3. Sort starts and ends
4. Init an empty list `ret`
5. Set occupied to 0
6. Set pointers s and e to 0
7. While s < len(starts) and e < len(ends),
    1. if starts[s] <= ends[e], increment occupied and s by 1 
    2. otherwise, 
        1. decrement occupied by 1
        2. if occupied is 0, append [ends[e], starts[s]] to ret
        3. increment e by 1
8. return ret
```
## Things I learned
- Neetcode's method of separating start and end times into two lists and iterating through them separately is a neat method with some cool applications
- I think this question was a lot easier because of my exposure to this method of solving merging interval-related problems
