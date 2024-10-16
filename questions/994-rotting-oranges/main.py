from typing import List

"""

m * n `grid`, each cell can have one of 3 values:
- 0 (empty cell)
- 1 (fresh orange)
- 2 (rotten orange)


every minute, every fresh orange next to (horizontally/vertically)
a rotten orange rots

return the minimum number of minutes until NO CELL HAS A FRESH ORANGE

edge cases:
- all empty cells or all rotten (0s/2s) => no fresh oranges to begin with, return 0
    - no 1s to begin with

- 1 or more fresh oranges, but no rotten oranges/no way for corruption to spread => return -1
    - infinite time for fresh orange to disappear

- in all other cases, return a non-zero integer indicating time taken to make all fresh oranges disappear

i want to try the multi-source BFS here


the sources will be the rotten oranges, since we can incrementally
count the total time it takes for the corruption to completely spread from there

however, there can be multiple rotten oranges => multiple sources

we will know the BFS has terminated once the queue of fresh oranges to process is empty
then we can look through our graph one last time to see if there are any remaining
fresh oranges
- these will be the unreachable ones, in which case we return -1

contamination only travels via adjacent fresh oranges, not through empty or already-rotten oranges
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        ROWS, COLS = len(grid), len(grid[0])

        queue = []
        visited = set()
        self.num_contaminated = 0

        def bfs(r: int, c: int):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] != FRESH or
                (r, c) in visited): return
            
            visited.add((r, c))
            queue.append((r, c))
            self.num_contaminated += 1

        fresh_count = 0

        # enqueue sources
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == ROTTEN: queue.append((i, j))
                elif grid[i][j] == FRESH: fresh_count += 1
        
        if fresh_count == 0: return 0

        # otherwise, there is at least 1 fresh orange
        # are there rotten oranges in their vicinity?
        
        time = -1
        while len(queue) > 0:
            for _ in range(len(queue)):
                r, c = queue.pop(0)
                visited.add((r, c))

                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            time += 1
        
        # at this point there exists at least 1 fresh orange, but not all of it was contaminated
        if self.num_contaminated != fresh_count: return -1
            
        return time

    # def isolated(self, r: int, c: int, grid: List[List[int]]) -> bool:
    #     ROWS, COLS = len(grid), len(grid[0])
    #     dirs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

    #     for d in dirs:
    #         if d[0] not in range(ROWS) or d[1] not in range(COLS): continue
    #         if grid[d[0]][d[1]] >= 1: return False
    #     return True

    
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))







