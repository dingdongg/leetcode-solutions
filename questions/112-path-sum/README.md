# 112 - Path Sum

## General Thoughts
- Easy

## Things to note
- Textbook application of DFS. Since we are looking for **root-to-leaf** sums, we can keep track of the progress of the sum up to any given node recursively
- When you recurse to the next level, pass `curr_sum + root.val` as the sum to the recursive calls 
- if this node has at least 1 child, it is **not** a leaf node, so you return the boolean OR between the left and right subtrees
    - otherwise, `root` would be a leaf node. Compare `curr_sum + root.val` to `targetSum` and return T/F based on results

### Performance

*Time* - `O(n)`, may end up traversing all nodes if the only valid path is the last path examined

*Memory* - `O(log(n))`, max call stack is proportional to the height of the tree

---

## Algorithm
```
1. Save targetSum as a global variable
2. call solve(root, 0)
3. solve(root, curr_sum):
    1. if root is defined, 
        1. set new_sum to curr_sum + root.val
        2. if root.left or root.right is defined (root isn't a leaf node),
            1. return solve(root.left, curr_sum + root.val) || solve(root.right, curr_sum + root.val)
        3. otherwise, return curr_sum + root.val == targetSum
    2. otherwise, return False
```