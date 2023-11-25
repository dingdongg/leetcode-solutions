# 110 - Balanced Binary Tree

## General Thoughts
- Slightly tricky, but really all it is is just adding one extra if-statement to record if the "balanced" state has been destroyed or not at each node

## Things to note
- See `# General Thoughts`

### Performance

*Time* - `O(n)`, we must check the height of each subtrees for each node

*Memory* - `O(log(n))`, memory allocation equal to the maximum height of the tree

---

## Algorithm
```
1. Set self.balanced to True
2. Call self.height(root)
3. def height(root):
    1. if root is null, return 0
    2. Set left_h to height(root.left)
    3. Set right_h to height(root.right)
    4. if abs(left_h - right_h) > 1, set self.balanced = False
    5. return 1 + max(left_h, right_h)
4. return self.balanced
```
## Things I learned
- Height of tree seems to be a pretty important feature in tree-related problems