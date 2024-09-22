from typing import List

"""

m * n island that is inbetween pacific & atlantic ocean:
    - pacific touches island's left/top edges
    - atlantic touches island's right/bottom edges

m * n 2D list `heights` - the height ABOVE SEA LEVEL at each coordinate in the island

when it rains, rainwater flows to neighboring cells (up/down/left/right)
if the neighbor cell's height <= current cell height

water can flow from any cell adjacent to an ocean into the ocean

return list of tuples `result` such that result[i] = (r_i, c_i) where 
rainwater can flow from cell (r_i, c_i) into BOTH oceans
- ie. the list of coordinates where rainwater from that source cell
      will enter both the pacific & atlantic oceans
    

ex1
            -P-
        [1 2 2 3 5]
        [3 2 3 4 4]
    -P- [2 4 5 3 1] -A-
        [6 7 1 4 5]
        [5 1 1 2 4]
            -A-

need to find the "out-of-bound" cells reached from each position in the grid

for (r, c), if r < 0 or c < 0 => pacific
            if r == m or c == n => atlantic

for each cell, BFS will give us the reachable ocean cells 
- we then use the above conditions to determine if it can reach both oceans

when r == 0 or c == 0 or r == m - 1 or c == n - 1, guaranteed
to reach at least one of the oceans
    - if c == n-1 and r == 0, both oceans
    - if c == 0 and r == m-1, both oceans

for a traversal from island cell to ocean, heights will be in non-increasing order

for a valid island cell (r, c), its neighbors can be one of the following cases:
    - out of bounds (ie. ocean)
    - island cell with greater height (not traversable)
    - island cells with <= height (traversable)

water only flows from cell->ocean, or A->B where height of A >= B

DFS actually sounds better
    - if a neighboring cell has already been computed and it turns out that:
        a. we can reach this neighbor
        b. that neighbor reaches both oceans
    - we can also reach both oceans from this current cell
    - BFS is iterative, but the above case requires recursive computations
        - if a cell has been seen before, we know which oceans it can reach
        - otherwise, we travel to all traversable neighbors

there are 4 states possible per cell:
- 0 oceans reachable
- pacific ocean reachable
- atlantic ocean reachable
- both oceans reachable

can be represented with 2 bits of info:
0 = no oceans
1 = pacific
2 = atlantic
3 = both

lets keep things simple

- run BFS on each island node
    - once it reaches an ocean node, update state accordingly
    - otherwise, enqueue neighbors and continue iterating until queue is empty

- if neighbor is traversable AND it has been computed before, 
    - copy its state over (ie. bitwise OR)

    
data structures required:
    - set to keep track of seen nodes
        - m * n 2D list of states (# oceans reachable)
per BFS task:
    - queue
    - mark node as seen at the very end when queue is empty

"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        compute the following collections:
            - nodes that can reach the pacific
            - nodes that can reach the atlantic
        
        return the intersection of the above two sets

        top row & left column are pacific ocean start nodes
        - from there, for each candidate node, do BFS/DFS
          to get other reachable nodes
        
        similarly, bottom row & right column are atlantic ocean start nodes
        """

        ROWS, COLS = len(heights), len(heights[0])
        # find pacific ocean reachables
        pacific, atlantic = set(), set()

        def bfs(r: int, c: int, ocean: set):
            queue = [(r, c)]

            while len(queue) != 0:
                row, col = queue.pop(0)
                if (row, col) in ocean: continue
                ocean.add((row, col))

                curr_h = heights[row][col]
                neighbors = [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]
                for nei in neighbors:
                    nr, nc = nei
                    if (nei in ocean or 
                        nr not in range(ROWS) or 
                        nc not in range(COLS) or
                        curr_h > heights[nr][nc]): continue
                    
                    # only add if not seen before AND height >= prev_h
                    queue.append(nei)

        for col in range(COLS):
            bfs(0, col, pacific)
            bfs(ROWS - 1, col, atlantic)

        for row in range(ROWS):
            bfs(row, 0, pacific)
            bfs(row, COLS - 1, atlantic)

        return list(pacific.intersection(atlantic))


    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     ROWS, COLS = len(heights), len(heights[0])
    #     PACIFIC, ATLANTIC = 1, 2
    #     res = []
            
    #     def dfs(r: int, c: int, h: int, seen: set) -> int:
    #         if (r, c) in seen: return 0

    #         ret = 0
    #         if r < 0 or c < 0: ret |= PACIFIC
    #         if r == ROWS or c == COLS: ret |= ATLANTIC

    #         # if not 0, we know we reached an ocean cell
    #         if ret != 0: return ret

    #         # h is the preivous height
    #         # in this case, water cannot flow from prev. cell to 
    #         # this current cell
    #         if heights[r][c] > h: return 0

    #         seen.add((r, c))
            
    #         ret |= dfs(r - 1, c, heights[r][c], seen)
    #         ret |= dfs(r + 1, c, heights[r][c], seen)
    #         ret |= dfs(r, c - 1, heights[r][c], seen)
    #         ret |= dfs(r, c + 1, heights[r][c], seen)

    #         seen.remove((r, c))
    #         return ret
    
    #     for row in range(ROWS):
    #         for col in range(COLS):
    #             if dfs(row, col, heights[row][col], set()) == 3:
    #                 res.append((row, col))

    #     return res


# heights = [[10,10,10],[10,1,10],[10,10,10]]
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(Solution().pacificAtlantic(heights))



         








