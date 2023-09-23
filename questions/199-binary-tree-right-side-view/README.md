# 199 - Binary Tree Right Side View

## General Thoughts
- Straightforward. I couldn't implement an iterative solution, but recursive version was easy

## Things to note
- The order of node traversals should be in post-order, since you want the rightmost nodes at each level in the tree
- we can use a dynamic array to keep track of the rightmost nodes at each level. if current `height` is equal to the length of the array, then the current node is the rightmost node for `height` (otherwise, height would be strictly less than the length of the array, which indicates that there was already a rightmost node that was marked previously)

---

### Performance

*Time* - `O(n)` to traverse all nodes in the tree

*Memory* - `O(log(n))`, equivalent to the height of the tree (max size of call stack possible)

---

## Algorithm
```
1. Init an empty array rightmost_nodes
2. call solve(root, 0)
3. solve(root, height):
    1. if root is defined,
        1. if height == len(rightmost_nodes), append root.val to rightmost_nodes
        2. call solve(root.right, height + 1)
        3. call solve(root.left, height + 1)
4. return rightmost_nodes
```