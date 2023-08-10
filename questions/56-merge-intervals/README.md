# 56 - Merge Intervals

## General Thoughts
- Pretty easy to my surprise, once I sat down and analyzed the problem it was smooth sail 😎

## Things to note
- When the intervals are drawn out on a number line, there are a few things to note:
    1. For any pair of intervals `A` and `B`, there are 6 possible cases:
        a. `B` is ahead of `A`, no overlap (`A_end < B_start`)
        b. `A` is ahead of `B`, no overlap (`B_end < A_start`)
        c. `B` is ahead of `A`, overlap occurs (`B_start in A`)
        d. `A` is ahead of `B`, overlap occurs (`A_start in B`)
        e. `B` engulfs `A` (`A in B`)
        f. `A` engulfs `B` (`B in A`)
    2. Cases a) and b) yield 2 distinct intervals
    3. For the other cases (c ~ f), the intervals merge into 1 in the following calculation:
        - `[min(A_start, B_start), max(A_end, B_end)]`
    4. If the intervals are sorted in non-decreasing order of their start values, all you have to do is compare adjacent interval pairs according to the logic above
        1. Have an array of computed intervals. As you loop through the array of intervals, compare each interval with the rightmost computed interval according to the logic in 1 and 3
- Thus, sorting is required
    - I tried to think what the solution would be like without sorting, and it seems like it would be a mess. There are `O(n^2)` pairs, and for every 2 pairs that are merged, you must re-compare them to every other interval again

### Performance

*Time* - `O(n log n)`, which is dominated by the sorting. Iterating through the pairs will take `O(n)`

*Memory* - `O(n)` to keep track of the computed intervals to return

---

## Algorithm
```
1. Sort the list of intervals in non-decreasing order of the interval start values
2. Init an array of intervals to return (ret), with the first interval inside it
3. For i from 1..len(intervals),
    1. Set top to be ret[-1], the rightmost computed interval thus far
    2. Set curr to be intervals[i], the current interval for comparison
    3. If curr's start is greater than top's end, no overlap. Append curr to ret
    4. Otherwise, intervals must merge. Set the top's end to max(top[END], curr[END])
4. Return ret
```
## Things I learned
- Establishing the most basic facts about the problem domain, making note of assumptions you make when you draw/sketch out a solution to the problem, really helps
    - In this problem, the most basic facts came from laying out the distinct cases possible for interval pairs
    - In this problem, I drew the intervals out on a number line and started comparing adjacent pairs for interval merging. *This came with the assumption that I had to operate on sorted interval lists*

## Things to improve
- To simulate interviews as much as possible, I should think out loud more as I solve problems