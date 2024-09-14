from typing import List

"""

given m * n bianry matrix `grid`
as before, 1 = land, 0 = water

land cells can be connected either horizontally or vertically

assume all 4 edges of the grid are surrounded by water

AREA OF ISLAND
= total number of land cells in that island

retrun the maximum area of an island in `grid`

if no islands, return 0


very similar to the counting islands question
will need to use graph traversal + set to keep track of visited nodes
- whenever we come across a new island, perform graph traversal to calculate the area 
  of that island
- keep track of a max variable and update this accordingly

"""


class Solution:
    def maxAareaOfIslandDFS(self, grid: List[List[int]]) -> int:
        """
        DFS solution
        """

        rows, cols = len(grid), len(grid[0])
        WATER, LAND = 0, 1
        visited = set()
        max_area = 0

        def dfs(r: int, c: int) -> int:
            if (r not in range(rows) or c not in range(cols) or
               grid[r][c] == WATER or (r, c) in visited):
                return 0
        
            visited.add((r, c))
            return 1 + (
                dfs(r, c - 1) +
                dfs(r + 1, c) +
                dfs(r, c + 1) +
                dfs(r - 1, c)
            )
        
        for i in range(rows):
            for j in range(cols):
                max_area = max(max_area, dfs(i, j))
        
        return max_area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        BFS solution
        """
        rows, cols = len(grid), len(grid[0])
        area = 0

        visited = set()

        queue = []

        def bfs(row: int, col: int) -> int:
            queue.append((row, col))
            ret = 0

            while len(queue) > 0:
                r, c = queue.pop(0)

                # node must not be visited
                # node must be land
                # node index must be valid
                if (r in range(rows) and c in range(cols) and 
                    (r, c) not in visited and grid[r][c] == 1):
                    ret += 1
                    visited.add((r, c))

                    # enqueue neighboring land cells
                    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
                    for d in dirs:
                        queue.append((r + d[0], c + d[1]))
            
            return ret

        for r in range(rows):
            for c in range(cols):
                area = max(bfs(r, c), area)
        
        return area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(Solution().maxAreaOfIsland(grid))
print(Solution().maxAareaOfIslandDFS(grid))