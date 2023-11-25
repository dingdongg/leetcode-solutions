# 100 - Same Tree

## General Thoughts
- Easy

## Things to note
- Every node value and their subtrees must all have the same values

### Performance

*Time* - `O(n)`, recursive function called at each node

*Memory* - `O(min(log(n), log(m)))`, minimum height of either tree

---

## Algorithm
```
1. if p and q are null, return True
2. else if p == None or q == None: return False
3. if p.val == q.val, return isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
4. return False
```