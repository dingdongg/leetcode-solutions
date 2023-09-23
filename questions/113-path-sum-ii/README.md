# 113 - Path Sum II

## General Thoughts
- Easy, little twist on [#112](https://leetcode.com/problems/path-sum/submissions/)

## Things to note
- As mentioned above, it is another DFS application + a little variation
- Maintain a stack that keeps track of the nodes on any given root-to-leaf traversal
    - if we reach a leaf node and find that `targetSum` equals `curr_sum + root.val`, push `root.val` to stack and add the stack to the return list
        - because of how python works, you need to instantiate a new list so that references to the stack aren't passed (which would lead to wrong answer)
- At every recursive call, if root is defined, we can append `root.val` to the stack and then pop it off the stack at the end of the call right before returning
    - this will return the stack to its original state before that function call, which is crucial in backtracking

### Performance

*Time* - `O(n)`, need to traverse all root-to-leaf paths, which is all nodes

*Memory* - `O(n log n)`. In the worst case, all root-to-leaf paths add up to target, which means we store `O(n)` paths, each of which are `O(log n)` in length

---

## Algorithm
```
1. Init an empty stack
2. Set targetSum as global variable
3. Init ret as an empty list
4. call solve(root, 0)
5. solve(root, curr_sum):
    1. if root is defined,
        1. push root.val to stack
        2. set new_sum to curr_sum + root.val
        3. if root.left or root.right is defined,
            1. call solve(root.left, new_sum)
            2. call solve(root.right, new_sum)
        4. otherwise,
            1. if new_sum == targetSum, append a copy of stack to ret
        5. pop from stack
6. return ret
```