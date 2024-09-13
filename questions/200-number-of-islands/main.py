from typing import List

"""

given an m*n 2D BINARY list of 1s and 0s, (1=land, 0=water),
return number of islands

ISLAND
- surrounded by water (0s)
- formed by connecting adjacent lands (1s) horizontally/vertically

assume that all 4 outer edges of grid is surrounded by water

there will a number of land cells in the grid (call this `l`)

if we look at a cell and it is a land, we can perform BFS to determine the size of that island
- once we get the size, we can subtract this amount from `l`

if `l` is now 0, we know that we looked at all land cells (ie. exhausted all islands)
otherwise if `l` > 0, there are islands we did not reach so we continue through the grid
until we arrive at yet another land cell we haven't visited
- this means we also need a set to keep track of the cells we previously visited 
- we only want to perform work on cells we have NOT visited

now that I think about it, we don't even need this `l`
- we simply perform BFS and keep track of the land cells we visited as part of this
- we skip looking at a cell if it is:
    1. a land cell we already visited
    2. a water cell
- otherwise, we increment the number of islands and perform BFS


DATA STRCUTURES
- queue for facilitating BFS
- set for keep tracking of visited nodes
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER, LAND = '0', '1'

        numIslands = 0
        visited = set()
        queue = []

        def bfs(r: int, c: int):
            queue.append((r, c))
            while len(queue) > 0:
                cell = queue.pop(0)
                if (cell[0], cell[1]) in visited or grid[cell[0]][cell[1]] == WATER: continue

                visited.add((cell[0], cell[1]))

                if (cell[0] - 1 >= 0): queue.append((cell[0] - 1, cell[1]))
                if (cell[0] + 1 < len(grid)): queue.append((cell[0] + 1, cell[1]))
                if (cell[1] - 1 >= 0): queue.append((cell[0], cell[1] - 1))
                if (cell[1] + 1 < len(grid[0])): queue.append((cell[0], cell[1] + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == LAND and (i, j) not in visited:
                    numIslands += 1
                    bfs(i, j)

        return numIslands
    
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))