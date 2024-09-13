# 51 - N-Queens

## General Thoughts
- conceptually the problem was pretty simple, but implementing the solution in code was difficult

## Things to note
- we keep track of the entire board state via a nested list
- a cell in this board can either be marked as *unoccupied*, *occupied*, or *dangerous*
    - *unoccupied* cells are neither dangerous nor occupied
    - *occupied* cells have been taken up by a queen
    - *dangerous* cells are empty cells where other queens cannot be placed (otherwise queens would attack each other)
- at each recursive call, we update the board state by placing the queen at the specified position
- then, we iterate through all empty lists and perform recursive DFS calls 
- however, since we have a nested list, in Python we must create a deep copy of the list with every iteration which is expensive (albeit constant)

### Performance

*Time* - `O(n^2 * 2^n)`, we perform `n^2` work at each node and there can be up to `2^n` nodes in total?

*Memory* - `O(n)`, the max length of the call stack is determined by `n`, the number of queens

---

## Optimization notes
- in a valid N-Queens board, each of the `n` queens are in a unique row/column/diagonal
    - Neetcode's video uses the concept of *negative* and *positive* diagonal indexes
        - *negative* diagonals are those that start from NW and go towards SE
            - this index can be calculated by checking `r - c`, since this value will be constant for the same diagonal
        - *positive* diagonals are those that start from SE and go towards NE
            - index can be calculated by checking `r + c`, this value will be constant for the same diagonal
    - with every queen we place at `(i, j)`, we can update these sets to mark which cells 
      have been occupied by a queen + any "dangerous" cells
    - if we check the sets with the respective indexes and find that at least one of our indexes are already
      present in the sets, then we know this cell is dangerous and a queen cannot be placed here
        - so, we proceed to the next column in the same row to see if we can place one there
- this is much more efficient because it lifts the entire process of managing and copying `n * n` nested lists at each iteration
    

### Performance

*Time* - `O(2^n)`, each node can potentially check up to `n` subnodes

*Memory* - `O(n)`, max length of the call stack is the number of rows of the board (ie. `n`)

---

## Algorithm
see `main.py` :)

## Things I learned
- visualizing this problem more would have helped 
