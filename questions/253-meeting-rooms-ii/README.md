# 253 - Meeting Rooms II

## General Thoughts
- Crazy hard, I could not figure it out for the life of me. And then neetcode video solved it in one go lol

## Things to note
- Assuming the intervals are drawn out horizontally on a number line, if you draw a vertical line through the intervals, the number of intervals that intersect with that vertical line is the number of rooms needed at that point in time
    - So, we want to find the **maximum** number of these intersects; doesn't matter when or which meetings, just the total count of max. rooms needed
- as you move this imaginary vertical line from left to right, whenever you encounter the start of an interval, the number of rooms would increase by 1
    - Similarly, whenever you encounter the end of an interval, the number of rooms decreases by 1
    - If a meeting ends and another starts at exactly the same time, compute the endtime first. This is because the 2 meetings are considered to be **not conflicting**
- To move through the start/endpoints sequentially in increasing order, we need 2 sorted lists: a list with start times and a list with end times
    - These will help simulate moving that vertical line from L->R

### Performance

*Time* - `O(n log n)`, to sort and compute the two lists required

*Memory* - `O(n)`, the sorted lists are the same size as the original input list

---

## Algorithm
```
1. Set starts to be a list that holds the start times from intervals in non-decreasing order
2. Set ends to be a list that holds the end times from intervals in non-decreasing order
3. Set indexes i and j to 0
4. Set max_so_far to -1
5. Set rooms to 0
6. While i < len(starts) and j < len(ends),
    1. if ends[j] <= starts[i], decrement rooms by 1 and increment j
    2. Otherwise, 
        1. increment rooms by 1
        2. set max_so_far to max(max_so_far, rooms)
        3. increment i
7. Return max_so_far
```
## Things I learned
- This problem taught me how to compute the number of overlapping intervals at any given point in time; it's a pretty neat way of thinking about overlapping intervals

## Things to improve
- I dug way too deep in the wrong direction. I was stubborn and tried to make my scuffed implementation working by hacking more and more things onto it, which made it even more complicated and killed my drive.
    - **SOLUTION: Starting off on a clean slate should help approach the problem in a different light. If I am too stuck, I should come back to the problem a few days later and re-attempt the problem (maybe look at the solution right after you decide to put it off for the day)**