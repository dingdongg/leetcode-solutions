# 457 - Circular Array Loop

## General Thoughts
- Pretty difficult, at one point I was just doing half-assed revisions to try and get the solution to pass lol, but managed to solve it in the end 

## Things to note
- When drawn out, any given array may have multiple cycles, both valid and invalid
    - Thus, you have to check whether the index you're on is included in a valid or invalid cycle
        - Invalid cycles are: 
            a. nodes that loop back to themselves (cycle w/ length = 1), OR
            b. cycles with both positive and negative directions (must either be all +ve or all -ve)
        - All other cycles are valid
    - As you check each index, add them to a set of seen indexes so that you skip it next time you see it to avoid duplicate work

### Performance

*Time* - `O(n)`, only `O(1)` operations are done for each index, and redundant indexes are skipped

*Memory* - `O(n)`, to keep a set of seen indexes

---

## Optimization notes
- Apparently this can be done with `O(1)` memory ??? I will have to come back to this some other time lol

### Performance

*Time* - ``

*Memory* - ``

---

## Algorithm
```
1. Init an empty set (seen_nodes)
2. For i in len(nums),
    1. If i is in seen_nodes, skip this iteration
    2. Set direction to 1 if nums[i] is positive, -1 otherwise
    3. Set slow and fast pointers to i
    4. Set length to 0
    5. add the slow pointer to seen_nodes
    6. While slow isn't equal to next_index(slow),
        1. If slow == fast and length > 1, return True
        2. Set slow to next_index(slow)
        3. Increment length by 1
        4. if nums[next_index(fast)] * direction < 0, break this loop
        5. Add next_index(fast) to seen_nodes
        6. Set fast to next_index(next_index(fast))
        7. if nums[fast] * direction < 0, break this loop
        8. Add fast pointer to seen_nodes
3. Return False 
```
## Things I learned
- I've noticed that I have gotten slightly better at recognizing certain patterns and applying the correct techniques to solve it efficiently
- The key in this question was to figure out the following:
    a. How to detect single-node cycles
    b. How to detect bidirectional cycles
    c. How to map a linked list traversal to this cyclic array traversal (=index calculations)
- Simple drawings are often the best, don't make it complicated as it makes it hard to recognize patterns

## Things to improve
- I noticed that whenever I fail to pass one of the base/edge cases, 90% of the time it is because of a small logical error in my code
    - For this example, in my `next_index()` helper, I incorrectly computed `len(nums) - added` instead of `len(nums) + added`
    - The issue was that I had *assumed* this part of my code (the helper function) was working properly, so I wasted time trying to debug other parts of my code
    - ***SOLUTION: WHEN TESTS DON'T PASS, THOROUGHLY REVIEW EVERY PART OF THE ALGORITHM AT LEAST ONCE, EVEN IF YOU THINK IT WORKS PROPERLY.***