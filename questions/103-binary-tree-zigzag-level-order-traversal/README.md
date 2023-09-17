# 103 - Binary Tree Zigzag Level Order Traversal

## General Thoughts
- Easy, but the ordering of elements was a little confusing to get right. Eventually got it 

## Things to note
- This is basic level-order traversal with one variation: switch up the order in which items are enqueued at each level!
    - even levels: add left child first, then right
    - odd levels: add right child first, then left
- for each level, key is to iterate from the back of the `curr_level` list
    - this allows us to reverse the order of the level nodes at each level

### Performance

*Time* - `O(n)`

*Memory* - `O(n)`

---

## Algorithm
```
1. Init an empty queue
2. If root node is defined, enqueue [root]
3. Set switch_order to True by default
4. Init an empty return list
5. While the queue isn't empty,
    1. Set curr_level to dequeued value
    2. Append a list of node values in curr_level to return list
    3. Init next_level to be an empty list
    4. While curr_level isn't empty,
        1. Set node to be popped value from curr_level
        2. if switch_order, append node.right then node.left
        3. otherwise, append node.left then node.right
    5. If next_level isn't empty, enqueue it
    6. Set switch_order to its negation
6. Return ret
```
## Things to improve
- Draw stuff out, it will help solve 1-off problems a lot more easily