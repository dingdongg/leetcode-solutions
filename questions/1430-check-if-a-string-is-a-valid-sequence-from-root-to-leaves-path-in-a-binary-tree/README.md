# 1430 - Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

## General Thoughts
- Easy

## Things to note
- Another application of DFS.
- the variation this time is that when the height of the tree is larger than the length of the array OR any node along a path doesn't match the corresponding value in the array, we short-circuit and return `False` for that path

### Performance

*Time* - `O(n)`; In the worst case, we have to check all root-to-leaf paths

*Memory* - `O(log(n))`; In the worst case, the call stack can grow proportional to the height of the tree

---

## Algorithm
```
1. Set arr to global variable
2. return solve(root, 0)
3. solve(root, height):
    1. if root is defined,
        1. if len(arr) <= height OR root.val != arr[height], return False
        2. if root.left or root.right is defined,
            1. return solve(root.left, height + 1) OR solve(root.right, height + 1)
        3. otherwise, return root.val == arr[height]
    2. otherwise, return False
```