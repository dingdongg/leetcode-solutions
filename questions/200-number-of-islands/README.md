# 200 - Number of Islands

## General Thoughts
- pretty straightforward
- the one thing that tripped me up was taht I thought I could implement BFS recursively,
  but BFS is best done iteratively w/ a queue data structure

## Things to note
- we are essentially counting the number of contiguous land cell chunks in the grid
- but, we don't want to "double count" any land cell we have previously seen
    - thus, we require a set to keep track of the visited nodes
- in order to find all of the contiguous land cells from a starting land cell,
  we need to use a graph traversal algorithm to find them
    - both DFS and BFS works
### Performance

*Time* - `O(n * m)`, we visit each node in the grid once and perform `O(1)` computations per node

*Memory* - `O(n * m)`, the visited node set can grow to include all nodes in the grid

---

## Algorithm
```
1. Set numIslands to 0
2. Create a set `visited`
3. Create an empty queue
4. def bfs(r, c):
    1. enqueue (r, c) to queue
    2. while the queue isn't empty,
        1. Set cell to the result of dequeueing queue
        2. if this cell was already visited or this cell is a water cell, continue
        3. mark this cell as visited
        4. enqueue all vertical/horizontal neighbors of cell that are within
           the bounds of the matrix
5. for i in 0..m:
    1. for j in 0..n:
        1. if (i, j) is a land cell and (i, j) has not been visited,
            1. increment numIslands by 1
            2. bfs(i, j)
6. return numIslands
```