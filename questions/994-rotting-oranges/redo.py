from typing import List

"""
m * n grid where each cell is one of 3 values:
- 0 (empty)
- 1 (fresh orange)
- 2 (rotten orange)

every minute, any fresh orange adjacent to a rotten orange becomes rotten

return min. time elapsed until NO CELL has a FRESH ORANGE
- if impossible, return -1

3 possible output categories:
    -1  (one or more fresh orange on board will never rot)
    0   (no fresh oranges to begin with, instantly reaches desired condition)
    > 0 (takes a non-zero length of time for all oranges to rot)
        - but fresh oranges are in a connected network with other oranges

ex1 (return 4)
2 1 1   2 2 1   2 2 2   2 2 2   2 2 2
1 1 0   2 1 0   2 2 0   2 2 0   2 2 0
0 1 1   0 1 1   0 1 1   0 2 1   0 2 2

2 1 1   2 2 1   2 2 2
1 1 0   2 1 0   2 2 0
0 1 2   0 2 2   0 2 2

ex2 (return -1)
2 1 1   2 2 1   2 2 2   2 2 2   2 2 2
0 1 1   0 1 1   0 2 1   0 2 2   0 2 2   ...
1 0 1   1 0 1   1 0 1   1 0 1   1 0 2

ex2 (return 0)
0 2 0
0 2 2
0 0 2

have a list of coordinates of the fresh oranges
    - if this list is empty, return 0 
run multi-source BFS (there can be more than one rotten orange), increment a counter for every breadth level traversed
    - do this until queue of nodes is empty
check all initial fresh orange coordinates; if any of them are still fresh, return -1
otherwise, return counter

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        fresh = []
        rotten = []

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1: fresh.append((i, j))
                elif grid[i][j] == 2: rotten.append((i, j))
        
        if len(fresh) == 0: return 0

        # otherwise, perform BFS
        def bfs(sources: List[tuple[int]]) -> int:
            queue = [sources]
            ret = 0

            while len(queue) > 0:
                nodes = queue.pop(0) # on first iteration, nodes will be rotten oranges
                next_nodes = []

                # rot all adjacent fresh oranges
                for n in nodes:
                    i, j = n
                    adj_nodes = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

                    for nn in adj_nodes:
                        x, y = nn
                        if (x in range(ROWS) 
                            and y in range(COLS) 
                            and grid[x][y] == 1):
                            grid[x][y] = 2
                            next_nodes.append(nn)
                
                if next_nodes: 
                    queue.append(next_nodes)
                    ret += 1
            
            return ret

        time = bfs(rotten)

        for orange in fresh:
            i, j = orange
            if grid[i][j] == 1: return -1
        
        return time
    

graph = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1],
]
print(Solution().orangesRotting(graph))