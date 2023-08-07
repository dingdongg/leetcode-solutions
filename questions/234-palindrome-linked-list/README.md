# 234 - Palindrome Linked List

## General Thoughts
- Straightforward, but the edge cases were annoying to deal with

## Things to note
- Remembering that the tortoise-hare method terminates when the slow pointer is 1/2 of the way through the linked list, you can store the nodes seen by the slow pointer in a stack as you iterate.
- Then when the fast pointer reaches null, iterate the slow pointer until the end, checking that the value popped from the stack is equal to the current slow pointer's node value

### Performance

*Time* - `O(n)`

*Memory* - `O(n)` due to the stack storing the first half of the linked list's values

---

## Optimization notes
- Can bring down to `O(1)` memory usage by reversing the second half of the array
- Once the slow pointer reaches the halfpoint, start reversing the remaining linked list
- Then, Compare the nodes from the original head and the new head, then increment them towards each other
    - Repeat until the pointers are equal/new head is null

### Performance

*Time* - `O(n)`, both the slow/fast + list reversing are `O(n)` operations

*Memory* - `O(1)`, just a few pointer variables - no stack required

---

## Algorithm
```
1. If the linked list only has 1 node, return True
2. If the linked list has 2 nodes, return head.val == head.next.val
3. Initialize slow and fast pointers to head
4. Initialize length to 1
5. While fast and fast.next are defined,
    1. Increment slow pointer by 1
    2. Increment fast pointer by 1
    3. Increment length by 1
    4. Increment fast pointer by 1
    5. If fast is defined, increment length by 1
6. Initialize prev pointer to be slow pointer if length is odd, None otherwise
7. Initialize jump poitner to be None
8. If length is odd, increment slow pointer by 1
9. While slow is defined,
    1. Set jump to slow pointer
    2. Set slow.next to prev pointer
    3. Set prev to slow pointer
    4. Set slow to jump pointer
10. Initialize second_head to prev pointer
11. Initalize _head to head
12. While second_head is defined and second_head != _head:
    1. if second_head.val != _head.val, return False
    2. Increment second_head and _head by 1 each
13. return True
```
## Things I learned
- Edge cases can be really annoying if not properly addressed

## Things to improve
- Always go through dry runs, which will help in addressing edge cases