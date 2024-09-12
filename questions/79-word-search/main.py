from typing import List

"""

given m x n matrix `grid` and string `word`, 
return true if `word` exists in grid

word can be formed from sequentially adjacent cells
- vertically/horizontally adjacent (=neighbors)

same cell cannot be used more than once

ex1
[A B C E]
[S F C S]
[A D E E]
"ABCCED"

v
A B C
    C
  D E
  ^

---

ex2
[A B C E]
[S F C S]
[A D E E]
"SEE"

       v
       S
     E E
     ^


backtracking problem

at each node in the decision tree, there will have been a previous trail of cells traversed
there are 2 possible cases:
    1. the current cell's value matches with the next letter of `word` to find
    2. the current cell's value DOES NOT match the next letter

in the first case, we continue traversing to try and build out the rest of the string
- we append the current cell's value to the traversed path and continue DFS style
otherwise, we terminate here and return False, since this path has been proved invalid (ie. unequal to `word`)

root node will have m * n children,
next child will have anywhere in between 0-4 children, etc...

1. finding root cell to start from
maintain a pointer to the next letter in the word `l` to search
look through the matrix and find all instances of `l`
- for every instance of `l` found, 
    - gather its neighbors
        - 
- if none found, return false


2. at every cell, there can be 1-3 choices for advancing to the next cell
3. if there are any subnodes that are equal to the next letter in the word (and has not been seen before),
    - mark it as seen and recursively traverse it

CONSTRAINT
- a cell can be used at most once
    - need a way to record the current sequence
        - a set?
        - a stack with DFS?    
    - at every node, we need to check if its child nodes have been traversed (ideally in O(1) time)
        - so, stack will be better for this (at the cost of a potentially expensive remove operation)
        - however, length of `word` is at most 15 characters, so maybe it's fine?

maintain a pointer that points to the next letter to look for in the matrix


"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()
        def solve(cell: tuple[int], path: List[str], i: int) -> bool:
            if i == len(word): return "".join(path) == word
            if cell in used: return False
        
            if board[cell[0]][cell[1]] == word[i]:
                used.add(cell)
                neighbors = []

                left = (cell[0] - 1, cell[1])
                right = (cell[0] + 1, cell[1])
                up = (cell[0], cell[1] - 1)
                down = (cell[0], cell[1] + 1)

                if left[0] >= 0: neighbors.append(left)
                if right[0] < len(board): neighbors.append(right)
                if up[1] >= 0: neighbors.append(up)
                if down[1] < len(board[0]): neighbors.append(down)


                path.append(word[i])
                if not neighbors: return "".join(path) == word

                for child in neighbors:
                    if solve(child, path, i + 1): return True
                path.pop()
                used.remove(cell)

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if solve((i, j), [], 0): return True
        
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
word = "ABCCED"


# board = [["a"]]
# word = 'a'

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

print(Solution().exist(board, word))