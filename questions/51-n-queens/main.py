from typing import List
"""

n * n chess board, goal is to place `n` queens inside that board
such that no queens can attack any other queen

given `n`, return all possible board layouts that satisfy the above goal 


ex1

n = 4
[
    [".Q.." "...Q" "Q..." "..Q."] A
    ["..Q." "Q..." "...Q" ".Q.."] B
]

A:
_ Q _ _
_ _ _ Q
Q _ _ _
_ _ Q _
    ^

B:
_ _ Q _
Q _ _ _
_ _ _ Q
_ Q _ _

within each inner list, items are sorted in rows from top to bottom of the board


a queen can attack any unit in its diagonals, vertical, or horizontal paths
from its current position

the queen marked with a caret (^) in layout A can attack the following coordinates:
- (1, 0) (2, 1) (2, 3)
- (3, 0) (3, 1) (3, 3)
- (0, 2) (1, 2) (2, 2)

at the beginning, an empty board starts with every cell as occupiable by a queen
after a queen is added at position (i, j) (assuming i, j are valid indexes),
- mark cells along its x-position as unoccupiable
- mark cells along its y-position as unoccupiable
- mark cells along its diagonals  as unoccupiable
- mark (i, j) as unoccupiable

at any point, if we still have queens left to place and there are no positions
on the board that are occupiable, then clearly this layout has failed - backtrack

we end up designing a decision tree to enumerate all valid board layouts,
with the root node being a completely empty board
- the height of the tree will be equal to n

for n=4,
- 4*4 = 16 choices for 1st queen placement
- <= 16 choices for 2nd queen placement

problem: "cleaning up" after each recursive call exits
- if we use one global 2D array to keep track of the occupancy state,
  we cannot "revert" back to the previous board state easily
    - when we make a recursive call, we can pass in as input 
      a separate copy of the previous board state?
    - OR we can keep track of the cells mutated in the current function call
      and clean up right before we return (but how?? this requires us to recall the previous state);
      i do not see this alternative working 
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        keep track of the following sets:
        - columns where queens are
        - negative diagonals where queens are
        - positive diagonals where queens are
        if I am trying to place a queen at (i, j)
        and this coordinate is present in any of the 3 
        sets above, that cell cannot be occupied by a queen

        this also removes the need to create a nested list
        to represent the board and having to copy it over
        in each recursive DFS call, so it is much more efficient

        set removals are also efficient, so cleanup after recursive calls
        can be done quickly as well
        """

        cols = set()
        # negative diagonal index: (r - c)
        negDiag = set()
        # positive diagonal index: (r + c)
        posDiag = set()
        pos = []

        layouts = []

        def solve(r: int, c: int, queens: int):
            if c >= n or r >= n: return

            nDiagIndex, pDiagIndex = r - c, r + c
            if c in cols or nDiagIndex in negDiag or pDiagIndex in posDiag:
                # try a different cell in the same row
                solve(r, c + 1, queens)
                return
            
            if queens == 0:
                # we have placed all queens
                pos.append((r, c))
                
                ret = []
                for p in pos:
                    row = ["."] * n
                    row[p[1]] = "Q"
                    ret.append("".join(row))
                layouts.append(ret)

                pos.pop()
                return
        
            # mark this cell as occupied
            cols.add(c)
            negDiag.add(nDiagIndex)
            posDiag.add(pDiagIndex)
            pos.append((r, c))

            solve(r + 1, 0, queens - 1)

            pos.pop()
            cols.remove(c)
            negDiag.remove(nDiagIndex)
            posDiag.remove(pDiagIndex)

            solve(r, c + 1, queens)
        
        solve(0, 0, n - 1)

        return layouts


    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     state = []
    #     layouts = []
    #     UNOCCUPIED, DANGEROUS, OCCUPIED = 0, 1, 2

    #     seen = set()
        

    #     for _ in range(n):
    #         row = [UNOCCUPIED] * n
    #         state.append(row)
        
    #     def solve(board: List[List[bool]], queens: int, r: int, c: int):
    #         if queens == 0 and board[r][c] == UNOCCUPIED:
    #             board[r][c] = OCCUPIED
    #             # no more queens left;
    #             # we terminate earlier when there are queens left but no options
    #             # to place on board, so we can assume the board is valid at this point.
    #             ret = []
    #             key = ""
    #             for row in board:
    #                 string = ""
    #                 for i in range(len(row)):
    #                     if row[i] == OCCUPIED: 
    #                         string += "Q"
    #                         key += str(i)
    #                     else: string += "."
    #                 ret.append(string)
                
    #             if key not in seen:
    #                 layouts.append(ret)
    #                 seen.add(key)
    #             return

    #         if (r < 0 or c < 0 or r >= n or c >= n or board[r][c]):
    #             return

    #         # verticals
    #         for y in range(n): board[y][c] = DANGEROUS
    #         # horizontals
    #         for x in range(n): board[r][x] = DANGEROUS

    #         # diagonals (do 4 directions separately)
    #         row, col = r - 1, c - 1
    #         while row >= 0 and col >= 0: # nw
    #             board[row][col] = DANGEROUS
    #             row, col = row - 1, col - 1
            
    #         row, col = r - 1, c + 1
    #         while row >= 0 and col < n: # ne 
    #             board[row][col] = DANGEROUS
    #             row, col = row - 1, col + 1

    #         row, col = r + 1, c - 1
    #         while row < n and col >= 0: # sw
    #             board[row][col] = DANGEROUS
    #             row, col = row + 1, col - 1

    #         row, col = r + 1, c + 1
    #         while row < n and col < n: # sw
    #             board[row][col] = DANGEROUS
    #             row, col = row + 1, col + 1

    #         board[r][c] = OCCUPIED
    #         # handle case where queens left, but nowhere to place on board
    #         empty_cells = []
    #         for i in range(n):
    #             for j in range(n):
    #                 if not board[i][j]: empty_cells.append((i, j))
            
    #         if len(empty_cells) == 0: return

    #         # valid indexes and there are empty cells on board
    #         for cell in empty_cells:
    #             board_copy = []
    #             for rr in board:
    #                 new_row = []
    #                 for cc in rr: new_row.append(cc)
    #                 board_copy.append(new_row)
    #             solve(board_copy, queens - 1, cell[0], cell[1])
            
    #     for i in range(n):
    #         for j in range(n):
    #             board_copy = []
    #             for rr in state:
    #                 new_row = []
    #                 for cc in rr: new_row.append(cc)
    #                 board_copy.append(new_row)
    #             solve(board_copy, n - 1, i, j)
        
    #     return layouts
    
print(Solution().solveNQueens(4))