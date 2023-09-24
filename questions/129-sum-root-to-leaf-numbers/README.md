# 129 - Sum Root to Leaf Numbers

## General Thoughts
- Easy

## Things to note
- Another variation on DFS. The global variable is an integer instead, which keeps track of the buildup of the number so far down the DFS path

### Performance

*Time* - `O(n)` to traverse all root-to-leaf paths

*Memory* - `O(log(n))` which is the height of the tree 

---

## Algorithm
```
1. set sum_so_far as global variable to 0
2. call solve(root, 0)
3. solve(root, prod):
    1. if root is defined,
        1. set new_prod to prod * 10
        2. set new_prod to new_prod + root.val
        3. if root.left or root.right is defined,
            1. call solve(root.left, new_prod)
            2. call solve(root.right, new_prod)
        4. otherwise, set sum_so_far to new_prod + sum_so_far
4. return sum_so_far
```