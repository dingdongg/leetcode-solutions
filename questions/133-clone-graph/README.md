# 133 - Clone Graph

## General Thoughts
- First graph question! (+ first LC question in 2 weeks :D) It was pretty difficult but overall fun

## Things to note
- The order of operations is crucial for everything to work here
- Basic structure is a BFS-like approach, where you create and store clones of the children of the source node in a dict
    - this is crucial as they prevent accidentally creating different clone objects of the same reference node; this will make it *seem* like everything's working as intended, since the nodes will have the same value but different memory addresses!
- Not sure if DFS approach would work, need to modify code to try it out later

### Performance

*Time* - `O(V)` - each vertex of the original graph is cloned and queued/popped once

*Memory* - `O(V)` - the queue can have all `|V|` vertexes in it at once, and the dict can grow to the size of `|V|`

---

## Algorithm
```
1. if node is null, return null
2. set newGraph to a new instance of Node(node.val, node.neighbors)
3. initialize an empty dict `created_nodes`
4. set created_nodes[newGraph.val] to newGraph
5. initialize a queue and enqueue newGraph
6. while the queue isn't empty,
    1. dequeue an node `newNode`
    2. initialize an empty array `newNeighbors`
    3. for neighbor in newNode.neighbors,
        1. set newNeighbor to created_nodes[neighbor.val], or a new Node(neighbor.val, neighbor.neighbors) if undefined
        2. append newNeighbor to newNeighbors
        3. if created_nodes[neighbor.val] is undefined,
            1. enqueue newNeighbor
            2. set created_nodes[neighbor.val] to newNeighbor
    4. set newNode.neighbors to newNeighbors from 6.2.
7. return newGraph
```
## Things I learned
- Graphs are pretty complicated to get right but it's the most fun I've had with LC questions so far lol
- Debugging at a memory level is painful to do with python

## Things to improve
- It might be useful to do a brief overview of graphs before I proceed with any more graph-related questions