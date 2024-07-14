# 84 - Largest Rectangle in Histogram

## General Thoughts
- did it a couple times in the past, feels a lot more straightforward now?

## Things to note
- MONOTONIC STACKS!!!
- given 2 bars of height `h` and `h'`, where index of `h` < index of `h'`, area can only be expanded horizontally IFF `h <= h'`
    - if `h > h'`, 2 possible areas:
        - `h * (j - i)`
        - `h' * (j - i + 1)`
- given the above, when we come across a bar such that its height is smaller than the previous bar, we can start executing area calculations
- if we keep these bars in a monotonically increasing stack (WRT height), we can calculate all plausible areas

### Performance

*Time* - `O(n)` - every bar is pushed to stack at most once, and all bars in the stack are popped once

*Memory* - `O(n)` - stack memory

---

## Algorithm
```
1. init an empty stack `bars`
2. set max_area = -1
3. for i in range(len(heights)),
    1. if bars is empty or height of bar at top of stack < heights[i],
        1. push (heights[i], i) onto `bars`
    2. elif bars isn't empty and height of bar at top of stack == heights[i], skip to next iteration
    3. else,
        1. set new_width = 0 
        2. while bars isn't empty and height of bar at top of stack >= heights[i],
            1. set b = bars.pop()
            2. set width = i - b[INDEX]
            3. new_width = width
            4. set area1 = width * b[HEIGHT]
            5. set area2 = (width + 1) * heights[i]
            6. set max_area = max(max_area, area1, area2)
        3. push (heights[i], i - new_width) onto `bars`
4. while bars isn't empty,
    1. set b = bars.pop()
    2. set w = i + 1 - b[INDEX] // i from step 3 stops at len(heights) - 1
    3. max_area = max(max_area, w * b[HEIGHT])
5. return max_area
```

## Things I learned
- monotonic stacks work best when I need to preserve an increasing/decreasing order of something
- in order to even figure this out, I have to understand the problem at hand well first
    - after that, having a rough idea of how to solve the problem can help suggest the appropriate data structures

## Things to improve
- still not comfortable with stacks ...