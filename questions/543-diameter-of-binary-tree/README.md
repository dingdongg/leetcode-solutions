# 543 - Diameter of Binary Tree

## General Thoughts
- Kinda tricky at first, but once I analyzed the problem in more detail it became clearer. Key is to dissect small, simpler cases of the problem first to find patterns!

## Things to note
- Important thing is that the diameter may not necessarily run through the rootmost node. This means I need a global variable to keep track of the maximum diameter seen in the tree and update it at each node if applicable
- assuming a height of `0` for null nodes and a height of `1` for a node with no children, the diameter of any given node is: `height(node.left) + height(node.right)`
    - use this to update the global max diameter variable if necessary

### Performance

*Time* - `O(n)`, `O(1)` work at each node for `n` nodes

*Memory* - `O(n)`, 1 call stack per node

---

## Algorithm
```
1. Init a dict max_so_far with one key-value pair (res: -1)
2. Call maxDepth(root, max_so_far)
3. maxDepth(root, maxSoFar):
    1. if root is null, return 0
    2. Set left_depth to maxDepth(root.left, maxSoFar)
    3. Set right_depth to maxDepth(root.right, maxSoFar)
    4. Set maxSoFar["res"] = max(maxSoFar["res"], left_depth + right_depth)
    5. Return 1 + max(left_depth, right_depth)
4. Return max_so_far["res"]
```
## Things I learned
- Don't underestimate the value of simple cases, they can provide valuable insight into finding a pattern for the entire problem