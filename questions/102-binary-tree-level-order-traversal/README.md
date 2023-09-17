# 102 - Binary Tree Level Order Traversal

## General Thoughts
- Very easy

## Things to note
- Level order of tree traversals require a queue
     - This also applies to BFS, since you're reaching every immediately adjacent nodes first, and then *their* unseen immediate neighbors, and so on

### Performance

*Time* - `O(n)`

*Memory* - `O(n)`, all nodes could be stored in the queue at once

---

## Algorithm
```
1. Initialize an empty queue (q)
2. Init an empty return list (ret)
3. If root is a node, enqueue [root]
4. While the queue isn't empty,
    1. set current_level to the dequeued value 
    2. append a list of values from nodes in current_level to ret
    3. Init an empty list (next_level)
    4. For each node in current_level,
        1. if node.left is defined, append node.left to next_level
        2. if node.right is defined, append node.right to next_level
    5. if next_level isn't empty, enqueue next_level
5. return ret
```