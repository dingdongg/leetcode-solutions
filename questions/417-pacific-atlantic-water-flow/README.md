# 417 - Pacific Atlantic Water Flow

## General Thoughts
- pretty damn hard, I was wound up on the brute force solution and couldn't figure out how to optimize

## Things to note
- Naive way is the perform traversal at every cell in the grid
- leads to redundant work since we are traversing over nodes multiple times potentially

### Performance

*Time* - `O((m * n)^2)` - full traversal will be `O(m * n)`, and we are executing this `O(m * n)` times

*Memory* - `O(m * n)` - max size of DFS call stack is the number of nodes in the grid

---

## Optimization notes
- Instead of performing a graph traversal per node in the grid, why not start at each ocean
  and figure out the nodes that can reach that particular ocean?
- we can compute two collections: unique points taht reach the atlantic, and unique points that reach the pacific
    - from here, we are interested in the intersection between these sets
- a lot faster too, since we can mark nodes as visited and need not visit them again in the future

### Performance

*Time* - `O(m * n)`, we are performing constant time work per node in the grid

*Memory* - `O(m * n)`, the sets we maintain can grow up to the number of cells in the grid

---

## Algorithm
```
1. set pacific and atlantic to be empty sets
2. def bfs(r, c, ocean):
    1. init a queue and enqueue tuple (r, c)
    2. while queue isn't empty,
        1. set node to dequeued value
        2. if node is in `ocean`, continue
        3. mark `node` as seen in `ocean`
        4. for every adjacent neighbor of `node`,
            1. if neighbor is in `ocean` or is out of bounds or height at the neighbor cell is less than the `node`'s height, continue
            2. enqueue neighbor
3. for c in 0..COLS-1,
    1. call bfs(0, c, pacific)
    2. call bfs(ROWS-1, c, atlantic)
4. for r in 0..ROWS-1,
    1. call bfs(r, 0, pacific)
    2. call bfs(r, COLS-1, atlantic)
5. return the intersection between `pacific` and `atlantic`
```
## Things I learned
- perspective shift can be OP (though I'm not sure how I could've achieved this on my own)

## Things to improve
- I took way too long to solve the problem
- don't ego my way out of the problem; if it's been a while without any progress, consider watching and studying the solution video