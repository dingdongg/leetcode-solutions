# 994 - Rotting Oranges

## General Thoughts
- Pretty straightforward

## Things to note
- DFS doesn't work because corruption spreads radially with respect to time, and DFS doesn't represent that 
- there can be multiple rotten oranges in the beginning, so multi-source BFS is best for this situation
- in `redo.py`, I also had a set to keep track of visited nodes. However, this is actually redundant since `grid` actually keeps track of visited nodes by converting fresh oranges into rotten ones. If a node is either empty or rotten, we can essentially think of them as "already traversed"

### Performance

*Time* - `O(n * m)`, each node is visited once and constant work is done per node

*Memory* - `O(n * m)`, the grid can theoretically be made of all fresh/rotten oranges

---

## Algorithm
see `redo.py`

## Things I learned
- Gotta stay consistent if I don't want to forget stuff like I did today 😵‍💫😵‍💫😵‍💫