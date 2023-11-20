# 226 - Invert Binary Tree

## General Thoughts
- very easy

## Things to note
- not much. Order at which you swap child nodes (bottom-up or top-down) doesn't matter

### Performance

*Time* - `O(n)`, worst case is an unbalanced (linear) binary tree of height `n`

*Memory* - `O(n)`, 1 call stack for each node in the tree

---

## Algorithm
```
1. if root is null, return root
2. store results of invertTree(root.left) in temp variable
3. store results of invertTree(root.right) in root.left
4. store temp in root.right
5. return root
```
## Things I learned
- GOTTA STAY ON THE GRIND

## Things to improve
- need to be more consistent with LC