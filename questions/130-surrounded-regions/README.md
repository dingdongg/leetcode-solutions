# 130 - Surrounded Regions

## General Thoughts
- very easy

## Things to note
- The problem statement makes it sound like there are 2 distinct conditions to look out for, but in essence it is just 1:
    - if you ever come across a region that has one or more of its cells on the border of the grid, it is not a capturable region
- neetcode further simplifies this problem by "inverting" the problem statement; instead of looking for capturable regions, he looks for (and marks) *uncapturable* regions (a region is either capturable or uncapturable, so this is a valid approach)

### Performance

*Time* - `O(n * m)`, each node is visited at most once and constant work is done per node

*Memory* - `O(n * m)`, the set to keep track of visited nodes

---

## Algorithm
```
1. init an empty set `seen`
2. def bfs(r, c):
    1. init a queue and enqueue tuple (r, c)
    2. init an empty list `region`
    3. set `capturable` to True
    4. while queue isn't empty,
        1. dequeue node; if in `seen`, continue
        2. append node to `region`
        3. for every adjacent neighbor, 
            1. if neighbor is in `seen`, continue
            2. if neighbor is out of bounds, set `capturable` to False and continue
            3. if neighbor cell is an "O", enqueue neighbor
    5. return [region, capturable]
3. for r in 0..ROWS-1,
    1. for c in 0..COLS-1, 
        1. if (r, c) not in `seen` and (r, c) is an "O" cell:
            1. set region, capturable to bfs(r, c)
            2. if capturable, iterate through region cells and mark as "X"
```
