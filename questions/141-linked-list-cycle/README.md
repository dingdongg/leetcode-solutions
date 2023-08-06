# 141 - Linked List Cycle

## General Thoughts
- Easy

## Things to note
- If a linked list has a loop, then the two pointers (slow and fast) are bound to loop back and meet one another on the same node
- If there is no cycle, the fast pointer will reach the end of the list and terminate

### Performance

*Time* - `O(n)`, the slow pointer may have to traverse through `n` nodes

*Memory* - `O(1)`, 2 variables for the slow and fast pointers

---

## Algorithm
```
1. Initialize slow and fast pointers to be the head of the given linked list
2. While the fast pointer isn't None and fast isn't pointing to None:   
    1. Move the slow pointer along 1 node
    2. Move the fast pointer along 2 nodes
    3. If the slow and fast pointers point to the same node, return true
3. return false
```
## Things I learned
- Not much, this was covered in DSA lecture
