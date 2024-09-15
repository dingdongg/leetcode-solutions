from typing import (
    List,
)

"""

m * n 2D grid `rooms` init'd with 3 possible values:
- wall/obstacle (-1)
- a gate (0)
- empty room (INF) (2^31 - 1)

fill each empty room with distance to NEAREST gate
- if a gate cannot be reached, room should be filled in with INF

assume that you can only move in the horizontal/vertical directions
(ie. no diagonal movement allowed; no "cutting corners")

shortest path calculation requires the use of BFS
DFS doesn't necessarily always yield shortest path from A to B


with each gate, we can propagate BFS and fill in neighboring
empty rooms iteratively with their distance to that gate
- if we encounter an "empty room" that already had a distance
configured, update it with the smaller distance value, since
we're interested in only the distance to the nearest gate

for empty rooms that are unreachable, it is fine to leave them
as is since the problem requires that we leave these values
as infinity

- queue to implement BFS

"""



class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        INF = pow(2, 31) - 1
        
        def bfs(r: int, c: int):
            queue = [(r, c, 0)]
            visited = set()

            while len(queue) > 0:
                row, col, dist = queue.pop(0)

                if (row not in range(ROWS) or 
                    col not in range(COLS) or 
                    rooms[row][col] == -1 or
                    (row, col) in visited): continue
                
                # if we come across a room visited in a previous BFS iteration,
                # and that old distance is smaller than the current distance, 
                # there is no need to traverse in that direction any further
                # because the distance in this current call of BFS will be 
                # guaranteed to be bigger (b/c it's always +1 per adjacent node)
                if rooms[row][col] != INF and dist > rooms[row][col]: continue

                rooms[row][col] = min(rooms[row][col], dist)
                visited.add((row, col)) 

                # enqueue neighboring rooms
                dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
                for d in dirs: queue.append((row + d[0], col + d[1], dist + 1))

        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0: bfs(i, j)
        
# grid = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
grid = [[0,-1],[2147483647,2147483647]]
Solution().walls_and_gates(grid)

print(grid)