# 111 - Minimum Depth of Binary Tree

## General Thoughts
- Straightforward

## Things to note
- At every level, you increment the possible result by 1
- Get the depth of the subtrees and choose the minimum between them

### Performance

*Time* - `O(n)`, must explore every node in the tree

*Memory* - `O(log(n))`, proportional to the height of the tree

---

## Algorithm
```
1. If root is null, return 0
2. If root.left and root.right are null, return 1
3. Set left depth to minDepth(root.left) or infinity
4. Set right depth to minDepth(root.right) or infinity
5. Return 1 + min(left_depth, right_depth)
```