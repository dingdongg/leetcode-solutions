# 104 - Maximum Depth of Binary Tree

## General Thoughts
- very easy

## Things to note
- return value must take the current node into account (hence the +1)

### Performance

*Time* - `O(n)`, go through every node in the tree

*Memory* - `O(n)`, 1 call stack per node

---

## Algorithm
```
1. if root is null, return 0
2. return 1 + max(maxDepth(root.left), maxDepth(root.right))
```