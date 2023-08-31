from typing import (
    List,
)

class DisjointSet:
    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n
        self.sets = n
    
    # find leader of set that i is affiliated with
    # implements path compression (ie. tree height is minimized)
    def find(self, i: int) -> int:
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    # join sets where first and second are affiliated to
    # implements union by size (ie. heuristic is height of set tree)
    def union(self, first: int, second: int):
        first_leader = self.find(first)
        second_leader = self.find(second)

        if first_leader == second_leader: return

        first_rank = self.ranks[first_leader]
        second_rank = self.ranks[second_leader]

        if first_rank < second_rank: self.parents[first_leader] = second_leader
        elif first_rank > second_rank: self.parents[second_leader] = first_leader
        else:
            self.parents[first_leader] = second_leader
            self.ranks[second_leader] += 1
        
        self.sets -= 1
    
    def num_sets(self) -> int:
        return self.sets

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # number of components is in the range [1, n]
        disjointSet = DisjointSet(n)

        for e in edges: disjointSet.union(e[0], e[1])
        
        return disjointSet.num_sets()

        # [0, 1, 2, 3, 4, ..., n - 1]
        # parent[i] is the direct parent of node i
        # if parent[3] = 15, then node 3 points to node 15


s = Solution()
n = 3
edges = [[0,1], [0,2]]
print(s.count_components(n, edges))




# [A, B], [B, C], [C, A], [D, E], [E, F]

# [A, B], [E, F], [C, A], [B, C], [D, E], [C, E]
#
# [A, B], [E, F], [C, A], [B, C], [D, E], [C, E]
# A
# B
# C
# D
# E
# F
#
# [E, F], [C, A], [B, C], [D, E], [C, E]
# AB
# C
# D
# E
# F
#
# [C, A], [B, C], [D, E], [C, E]
# AB
# C
# D
# EF
#
# [B, C], [D, E], [C, E]
# ABC
# D
# EF
#
# [D, E], [C, E]
# ABC
# D
# EF
# 
# [C, E]
# ABC
# DEF
# 
#
# ABCDEF
# 
s = """
A

        C

    B

    

    
    D         E      F


"""




