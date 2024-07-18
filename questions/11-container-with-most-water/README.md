# 11 - Container With Most Water

## General Thoughts
- easy

## Things to note
- with the two-pointer technique, you avoid the `O(n^2)` runtime because with each iteration,
you're essentially trying to improve the bottleneck (ie. the minimum height between two bars)
in order to maximize the area
- the left and right pointers are initialized at the left and right ends of the bars array.
This is because this will maximize the width - if it happens that the outermost bars are the 
two tallest bars in the graph, then by default this will be the maximum area returned. The only
way for any inner areas to be greater is to have a "significantly" larger height

### Performance

*Time* - `O(n)`

*Memory* - `O(1)`

---

## Algorithm
```
1. set l, r = 0, len(height) - 1
2. set max_area = 0
3. while l < r,
    1. set area = (r - l) * min(height[l], height[r])
    2. max_area = max(max_area, area)
    3. if height[l] < height[r] increment l by 1 (l points to the bottleneck)
    4. otherwise, decrement r by 1 (r points to the bottleneck, or they're equal in which case it doesn't matter which pointer you update)
4. return max_area
```