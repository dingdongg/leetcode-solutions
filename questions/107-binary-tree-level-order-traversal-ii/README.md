# 107 - Binary Tree Level Order Traversal II

## General Thoughts
- Very easy

## Things to note
- Problem with using queues again for this problem (like [#102](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)) is that there is no easy way to identify the level of any enqueued node
- having a recursive solution that explicitly returns a list of bottom-up level-order nodes is infeasible for the same reason (there is no way to tell apart the nodes in the returned list, in terms of their level)
- thus, having a list in a global context to store the nodes seen so far at any given level will be beneficial (in this problem I used an instance field)
    - Basically, you first recurse on the children to add them to their respective levels. Then you can record the root value to the current level
    - whenever `level` is equal to the global context list length, we can append another empty list to dynamically grow this global context variable as we encounter more and more levels in the tree

### Performance

*Time* - `O(n)`

*Memory* - `O(n)`, 1 call stack per node + levels array total contents

---

## Algorithm
```
1. Init an empty list (levels)
2. Call bottomUp(root, 0)
3. bottomUp(root, level):
    1. if root is defined,
        1. if level == len(levels), append empty list to levels
        2. Call bottomUp(root.left, level + 1)
        3. Call bottomUp(root.right, level + 1)
        4. append root.val to levels[level]
4. reverse levels and return it
```
## Things I learned
- Level order doesn't necessarily imply the use of a queue DS
    - ie. **DON'T COMPLETELY LOCK YOURSELF INTO USING A PARTICULAR DS!**