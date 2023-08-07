# 143 - Reorder List

## General Thoughts
- Easy, drawing out the final linked list for longer examples really helped

## Things to note
- The end result linked list has pointers re-arranged in a "zig-zag" fashion
    - for the following list,
        ```
        0 -> 1 -> 2 -> ... -> n-2 -> n-1
        ```
    - node `0` points to node `n-1`, node `n-1` points to node `1`, node `1` points to node `n-2`, node `n-2` points to node `2`, etc...
- In order to achieve this, we require the following pointers:
    - a pointer to the head node (=current)
    - a pointer to the current node's **old** next node
    - a pointer to the current node's **new** next node
    - a pointer to the next head value
- We want the next head pointer to be alternating back and forth in our linked list, going inwards by 1 each iteration. This means that we need our linked list to point inwards from both either ends
    - this means that we need to reverse the direction of the second half of the list
    - can achieve this using tortoise-hare to stop at midpoint, and reversing the rest as needed
- Once reversed, we can manipulate the list using the 4 pointers mentioned above and working inwards

### Performance

*Time* - `O(n)` - tortoise-hare, reversing list, pointer manipulations are all `O(n)` operations

*Memory* - `O(1)`, a few pointer variables required

---

## Algorithm
```
1. If the list has 1 or 2 nodes, the list is already reordered so return
2. Init slow and fast pointers to head
3. While fast and fast.next are defined,
    1. Increment slow pointer by 1
    2. Increment fast pointer by 2
4. Init prev pointer to None
5. Init jump pointer to None
6. While slow pointer is defined,
    1. Set jump to slow.next
    2. Set slow.next to prev pointer
    3. Set prev to slow pointer
    4. Set slow to jump pointer
7. Init next_head to prev pointer
8. Init _head to head pointer
9. While _head != jump:
    1. Set jump to _head.next (jump will point to current node's old next)
    2. Set _head.next to next_head pointer
    3. Set _head to next_head pointer
    4. Set next_head to jump pointer
```
## Things I learned
- Drawing examples out always helps :)
- Linked list related questions mostly seem to utilize either one of tortoise-hare, reversing linked list, or a combination of both (plus some variations)
- The final step (zigzag pointer manipulation) seemed pretty daunting, but walking through an example from start to finish really helped in terms laying out each step of the algorithm
