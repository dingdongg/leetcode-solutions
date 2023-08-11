# 986 - Interval List Intersections

## General Thoughts
- Pretty straightforward, did a solid analysis of the problem and the logic was concrete

## Things to note
- Remember that, between two arbitrary intervals `A` and `B`, there are 6 distinct cases. 
    - 2 non-overlaps (A ahead of B, B ahead of A)
    - 2 partial overlaps (A ahead of B, B ahead of A)
    - 2 engulfs (A engulfs B, B engulfs A)
- A naive approach to solving this problem is to take every interval in `firstList` and compare it to every pair in `secondList`
    - If there are overlaps in between, push them to a ret list and check the next interval pair
- There are `O(n * m)` pairs across the two lists which makes this approach inefficient
- intersections are calculated by: `[max(A_start, B_start), min(A_end, B_end)]`

### Performance

*Time* - `O(n * m)`

*Memory* - `O(max(len(n), len(m)))` to hold the list of intersections, of which there could be `max(len(n), len(m))` in total

---

## Optimization notes
- In the brute force method, the redundant calculation comes from the fact that, if intervals `l1[i]` and `l2[j]` don't overlap, then intervals `l2[j:]` won't either; so we can skip these iterations
    - at this point, we can increment the index pointing to the interval that comes *earlier* than the other
- For all pairs that do overlap, we increment the index pointing to the interval with an **earlier end value**
    - it doesn't make sense to do it the other way around, since your interval pairs would become farther apart (and could potentially miss out on other pairs that overlapped with the interval that came before)
- The lists are sorted in non-decreasing start values already, so we can start from the beginning of each list
    - calculate overlaps (if any), and increment pointers accordingly

### Performance

*Time* - `O(n + m)` as you iterate through both lists once

*Memory* - `O(max(len(n), len(m)))` to hold the list of intersections, of which there could be `max(len(n), len(m))` in total

---

## Algorithm
```
1. If the first or second list is empty, return []
2. Set ret to empty list
3. Set indexes i and j to 0
4. While i < len(firstList) and j < len(secondList),
    1. Set earlier_interval to firstList[i] if first comes before second, otherwise secondList[j]
    2. Set later_interval to whatever you didn't assign to earlier_interval
    3. if earlier_interval's end is less than the later interval's start, 
        1. Increment i by 1 if earlier is from firstList, otherwise increment j by 1
        2. continue
    4. Append [max(earlier[START], later[START]), min(earlier[END], later[END])] to ret
    5. Increment the index pointing to the interval that ends earlier 
5. Return ret
```
## Things I learned
- The fundamentals around intervals don't seem to change much with different variations on the problem
- Even though I knew the 6 distinct cases, walking through each of them one by one again helped me plan out how to handle each case, which led me to discover ways I can shrink the amount of code written

## Things to improve
- I have to be more alert to catch small mistakes that keep slipping by
    - For instance, incrementing both `firstList` and `secondList` with `i` accidentally
    - Forgetting to handle non-overlap cases
    - How I assumed the first list items are always the earlier interval when trying to determine whether to increment `i` or `j` at the end
    - **SOLUTION: GET MORE SLEEP, OR DO THESE PROBLEMS WHEN YOU'RE NOT TIRED**