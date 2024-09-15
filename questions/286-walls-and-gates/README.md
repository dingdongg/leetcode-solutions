# 286 - Walls and Gates

## General Thoughts
- pretty straightforward, almost missed one crucial condition though

## Things to note
- BFS can help calculate the shortest-path distance from a source node to all other reachable nodes
- by performing BFS from each gate in the grid, we can then calculate the shortest path to the nearest gate
    - this leads to `g` BFS calls, where `g` is the number of gates in the grid
    - in any BFS call, if we come across a room whose shortest path had already been calculated, there are 2 options:
        1. the old distance > the distance to the current gate
            - this means that all subsequent rooms in this direction will be closer to the current gate than the previous gate
            - thus, continue traversal in this direction
        2. the old distance <= the distance to the current gate
            - this means that all subsequent rooms in this direction will be farther from the current gate (guaranteed)
            - this is because distance is incremented by 1 per level
            - thus, stop traversal in this direction to avoid redundant calculations and save time
- Neetcode seems to perform *multi-source BFS* - look into that?

### Performance

*Time* - `O((m * n)^2)`, worst case is where every node is a gate OR we iterate through gates in a way where we continuously overwrite the previous shortest paths, leading to us traversing the entire graph multiple times

*Memory* - `O(m * n)`, used to keep track of the visited nodes

---

## Algorithm
see `main.py`

## Things I learned
- for BFS, it's important to use a set to keep track of the visited nodes so we don't end up in an infinite loop
