from typing import List

"""

m * n `board` containing "X" and "O"

goal is to CAPTURE REGIONS that are SURROUNDED

- cells are connected to neighbor cells horizontally/vertically (connectivity)
- regions are formed by connecting all neighboring "O" cells (region)
- region is surrounded if:
    - region can be connected with "X" cells AND 
    - none of the region cells are on the edge of the board

to "capture" a region, replace all region cells with "X" 
in the original board

region discovery: simple BFS
- if we go out of bounds, we know one of the region cells is on the edge

we can have BFS return all cells in the given region
- use this to capture region if none were on the edge


"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        seen = set()

        # make this function simply return the entire region
        # then in the nested for loop below this function
        # definition, we can mark them as visited
        def bfs(r: int, c: int) -> list:
            queue = [(r, c)]
            region = []
            capturable = True

            while len(queue) != 0:
                row, col = queue.pop()
                if (row, col) in seen: continue
                seen.add((row, col))
                region.append((row, col))

                neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
                for nei in neighbors:
                    nr, nc = nei
                    if nei in seen: continue
                    if (nr not in range(ROWS) or
                        nc not in range(COLS)): 
                        capturable = False
                        continue

                    if board[nr][nc] == "O": queue.append(nei)
            
            return [region, capturable]
    
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in seen and board[row][col] == "O":
                    region_cells, capturable = bfs(row, col)

                    if capturable:
                        for cell in region_cells:
                            board[cell[0]][cell[1]] = "X"


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)
print(board)

            
                    


board = [
    ["X","O","O","X","X","X","O","X","O","O"],
    ["X","O","X","X","X","X","X","X","X","X"],
    ["X","X","X","X","O","X","X","X","X","X"],
    ["X","O","X","X","X","O","X","X","X","O"],
    ["O","X","X","X","O","X","O","X","O","X"],
    ["X","X","O","X","X","O","O","X","X","X"],
    ["O","X","X","O","O","X","O","X","X","O"],
    ["O","X","X","X","X","X","O","X","X","X"],
    ["X","O","O","X","X","O","X","X","O","O"],
    ["X","X","X","O","O","X","O","X","X","O"],
]