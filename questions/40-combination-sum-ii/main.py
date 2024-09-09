from typing import List

"""
given a list of numbers `candidates` and target number `target`, 
find ALL unique combinations where candidate numbers sum to `target`


CONSTRAINTS:
- no duplicate combinations allowed in solution set

ex1
[10 1 2 7 6 1 5], target = 8

[
    [1 7]
    [2 6]
    [1 2 5]
    [1 1 6]
]

need to enumerate all possibilities
will need to formulate a decision tree

at every node, a candidate number `c` will be up for consideration
- there are 2 choices:
    1. include `c` in the current sequence
    2. exclude `c` from current sequence

this will generate a tree with everyh element from the power set as leaf nodes
= O(2^n) nodes

a given node builds off of its parent node, so the sum can be 
calculated in constant time

[10 1 2 7 6 1 5], target = 8

[
    [1 7]
    [2 6]
    [1 2 5]
    [1 1 6]
]

1 2 5
1 7
1 6 1
2 6

root node: [], sum = 0
    - [10], sum = 10; backtrack
    - [], sum = 0
        - [1], 1
            - [1 2], 3
                - [1 2 7], 10; backtrack
                - [1 2 6], 9; backtrack
                - [1 2 1], 4
                    - [1 2 1 5], 9; backtrack
                - [1 2 5], 8; add to solution set
            - [1 7], 8; add to solution set
            - [1 6], 7
                - [1 6 1], 8; add to solution set
                - [1 6 5], 12; backtrack
            - [1 1], 2
                - [1 1 5], 7
            - [1 5], 6
        - [], 0
            - [2], 2
                - [2 7], 9; backtrack
                - [2 6], 8; add to solution
                - [2 1], 3
                    - [2 1 5], 8 (already recorded)
                - [2 5], 7
            - [], 0
                - [7], 7
                    - [7 6], 13; backtrack
                    - [7 1], 8 (already recorded)
                    - [7 5], 12; backtrack
                - [], 0
                    - [6], 6
                        - [6 1], 7
                            - [6 1 5], 12; backtrack
                        - [6 5], 11; backtrack
                    - [], 0
                        - [1], 1
                            - [1 5], 6
                        - [], 0
                            - [5], 5
                            - [], 0

duplicate elements may exist;
- can lead to redundant computation
- at each node in the tree, compute an immutable key
- use that key to find whether or not this node has already been visited
    - if yes, skip
    - if no, compute and record
- will need a dictionary for this
- key will be computed by creating a static list of length 51, then recording the frequency of each numnber in the current sequence
    - converted to a tuple for immutability (keys in dicts must be immutable)

    
this is DFS backtracking, will need to use a stack
- lists in python support common stack operations
"""

# class Solution:
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     seen = {}
    #     ret = []

    #     def computeKey(seq: List[int]) -> tuple:
    #         freq = [0] * 51
    #         for n in seq: freq[n] += 1
    #         return tuple(freq)


    #     def solve(seq: List[int], start: int, sum_so_far: int):
    #         # handle potential `start` overflow                
    #         # first compute the key
    #         key = computeKey(seq)

    #         if start >= len(candidates): # reached leaf node
    #             if key not in seen:
    #                 seen[key] = True
    #                 if sum_so_far == target: ret.append(list(seq))
    #             return

    #         if key not in seen:
    #             seen[key] = True
    #             # not seen yet, compute and record
    #             # ONLY IF sum_so_far < target;
    #             # if equal to target, record and just return
    #             # if greater, return (ie. "backtrack")
    #             if sum_so_far < target:
    #                 for idx in range(start, len(candidates)):
    #                     seq.append(candidates[idx])
    #                     solve(seq, idx + 1, sum_so_far + candidates[idx])
    #                     seq.pop()
    #             elif sum_so_far == target:
    #                 # add to solution set
    #                 ret.append(list(seq))
                
    #             # check node as visited and return
    #         # tree has been traversed already, skip
        
    #     solve([], 0, 0)
    #     return ret

"""
^^^^^
expensive part of my first approach was the fact that i had to compute an expensive key
- this is because I was traversing every possible combination/permutation possible for sums < target
- we can draw on the insights from combination sum I and 3sum to eliminate duplicates

in combination sum I, the key finding was that we have 2 choices with each element i:
- generate a subnode that will recursively find all combinations with AT least one instance of i
- generate a subnode that will recursively find all combinations with ZERO instances of i

this helped get rid of duplicates, however:
- in this problem, a number at a given index can only be used at most once
- what this means is that for the subnode that decides to include i, the recursive sequences generate will have EXACTLY ONE INSTANCE of i
- note that we're only concerned with duplicate indexes; numbers themselves dont matter as long as they add up to target

in 3sum, duplicates were eliminated because:
- we sorted the list and skipped elements we already saw when choosing the first index
- when finding the corresponding pair of numbers for a chosen index, 
  we also removed duplicates by modifying the left/right pointer updates to skip duplicates

so if we sort this input list, we can use a similar method to skip duplicates

[10 1 2 7 6 1 5], target = 8
[1 1 2 5 6 7 10]

[] 0
    - [1] 1
        - [1 1] 2
            - [1 1 2] 4
                - [1 1 2 5] 9 XXX
            - [1 1 5] 7
                - [1 1 5 6] 13 XXX
            - [1 1 6] 8 RECORD (technically whenever we record, we can return without continuing to check future elements, since the sum can only grow bigger (or be a duplicate))
            - [1 1 7] 9 XXX (we can actually just straight up return here, since all future elements will make the sum >= the sum here)
        - [1 2] 3
            - [1 2 5] 8 RECORD
        - [1 5] 6
            - [1 5 6] 12 XXX
        - [1 6] 7
            - [1 6 7] 14 XXX
        - [1 7] 8 RECORD
    - [1 <- index=1] 1 XXX
        - this will be a subtree of the already-computed tree before it, can skip
    - [2] 2
        - [2 5] 7
            - [2 5 6] 13 XXX
        - [2 6] 8 RECORD
    - [5] 5
        - [5 6] 11 XXX
    - [6] 6
        - [6 7] 13 XXX
    - [7] 7
        - [7 10] 17 XXX
    - [10] 10 XXX

notice that there were no duplicate solutions being recorded
- when the sum is greater than our target, we halt any further DFS traversals
- when the sum is equal to target, we record our answer and halt any further DFS traversals
    - in both cases, this is because the sum will only get bigger (or be a duplicate solution)
- when we come across a duplicate number (ie. a number whose immediate neighbor to the left is the same number),
  just simply skip all duplicate instances until we reach a new number and repeat the process
    - this is the reason we are able to avoid all future duplicates (also the sorting helps achieve this)

"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []

        def solve(seq: List[int], i: int, sum_so_far: int):
            if i >= len(candidates): 
                if sum_so_far == target: ret.append(list(seq))
                return 

            if sum_so_far < target:
                idx = i
                while idx < len(candidates):
                    seq.append(candidates[idx])
                    solve(seq, idx + 1, sum_so_far + candidates[idx])
                    seq.pop()
                    idx += 1
                    while idx < len(candidates) and candidates[idx] == candidates[idx - 1]:
                        idx += 1
            elif sum_so_far == target:
                # record
                ret.append(list(seq))
        
        solve([], 0, 0)
        return ret
    



# candidates = [10,1,2,7,6,1,5] 
# target = 8

candidates = [2, 5, 2, 1, 2]
target = 5
print(Solution().combinationSum2(candidates, target))