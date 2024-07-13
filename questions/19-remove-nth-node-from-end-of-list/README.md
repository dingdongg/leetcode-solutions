# 19 - Remove Nth Node From End of List

## General Thoughts
- pretty easy, just had minor issues patching up edge cases

## Things to note
- one downfall of a basic linked list is the O(n) access time for a random node
- thus, 1 `O(n)` traversal needed to figure out the length of the list
- use `length - n` to figure out the index of the node to delete
- then, iterate through the linked list again, stop at the target node, and re-arrange pointers

### Performance

*Time* - `O(n)`

*Memory* - `O(1)`, just some pointers and counter variables

---

## Optimization notes
- in order to solve this in **ONE** traversal, we require `O(1)` random access
- to achieve this, we can store each node in an array
- we use the 1 traversal to store every node in the array, thereby getting its length too
- now we can just grab the target node in `O(1)` time

### Performance

*Time* - `O(n)` still, but 1 traversal only as opposed to 2

*Memory* - `O(n)`, the backing array to store each node

---

## Algorithm
```
1. if head.next is null, we have a LL of length 1. return None
2. Init an empty array (nodes)
3. Set curr = head
4. While curr is not None,
    1. append curr to nodes
    2. Set curr = curr.next
5. Set target = len(nodes) - n
6. if target is 0, return nodes[1]
7. otherwise, set nodes[target - 1].next = nodes[target].next
8. return nodes[0] 
```
## Things I learned
- In this problem, thinking about the downsides of LL & how to overcome this disadvantage led me to the optimization naturally

## Things to improve
- staying consistent :c