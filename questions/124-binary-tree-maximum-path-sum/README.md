# 124 - Binary Tree Maximum Path Sum

## General Thoughts
- Pretty complicated, but somehow I managed to solve it :o (although I was bottom 5% runtime perf)

## Things to note
- the max path sums we get back from its subtrees may be of 3 types (in retrospect, maybe types A and C may be grouped together? not 100% sure tho). Depending on the path type, our answer may vary:
    1. type A - the path is a "double path", which is completely contained within the subtree (but doesn't include the subtree root)
        - this would also include the type Bs without linking the current node
    2. type B - the path is a "single path", which forms a linear chain of nodes + the subtree root
    3. type C - the path is again a "double path", but it includes the subtree root as well
        - this is formed by just the root alone, or by linking the left and right type Bs together
- constraints:
    1. the path may not necessarily pass through the root of the tree
    2. each node can only appear in the sequence at most once (ie. no backtracking allowed)

- thus, if we find a double path in an immediate child subtree, we can't link it up with the current node because this breaks constraint #2 (you have to backtrack to include both left and right subtrees, and then link it to a parent node as well)

```
is the max sum path self-contained within the left/right subtree?
- if so, the current node should not be considered
- but what if by including the current node, the parent node can join it up with another tree
  for a total sum that is substantially bigger than what was originally possible?

  - this means that, at each node, we need to be able to configure whether or not 
    we want to include the current node we're at in the max sum path calculation.
```
^ the above is why I consider all 3 types in my solution and return them to the caller (since this max calculation must be executed by the parent node as well)

### Performance

*Time* - `O(n)`, we perform `O(1)` work per node and visit each node once

*Memory* - `O(log(n))`, max memory usage is proportional to the height of the tree as that dictates the maximum size of the call stack

---

## Optimization notes
- TODO? not sure if this can be optimized

### Performance

*Time* - ``

*Memory* - ``

---

## Algorithm
```
1. return max(maxpath(root))
2. define maxpath(root) -> [int, int, int]:
    1. if root is None, return [-inf, -inf, -inf]
    2. set left_sums to maxpath(root.left)
    3. set right_sums to maxpath(root.right)
    4. set type_a to max of:
        - left_sums[0]
        - right_sums[0]
        - left_sums[1]
        - right_sums[1]
    5. set type_b to max of:
        - left_sums[1] + root.val
        - right_sums[1] + root.val
        - root.val
    6. set type_c to max of:
        - left_sums[2]
        - right_sums[2]
        - root.val
        - left_sums[1] + right_sums[1] + root.val
    7. return [type_a, type_b, type_c]
```
## Things I learned
- OBSERVATION METHOD IS SUPER OP
- analyzing the problem thoroughly before moving onto the code is crucial so that I don't 
get wound up with a scuffed solution and rage quit

## Things to improve
- I still tried to prematurely move onto the code, and considering this was a hard difficulty question,
I should have spent more time to analyze the question until I had a lot more confidence in my logic