from typing import List

"""
formuilate a decision tree
also need to filter out duplciates
naive way: compute an immutable key containing info about the frequency of items in the sequence
- constant time, but still expensive operation

work around this by creating a mindful decision tree that will never
generate redundant nodes
- at each node, you have 2 options:
    - include an element i
    - exclude element i
- however, you can augment this further to eliminate duplicates:
    - when you include i, you're saying that all subnodes in that direction
      will have AT LEAST one instance of i
    - when you exclude i, you're saying that all subnodes in that direction
      will have ZERO instances of i, always
    - these are the tree invariants, and must be upheld recursively at all nodes
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        # idx keeps track of the position of the element for consideration
        def solve(seq: List[int], idx: int, sum_so_far: int):
            if idx == len(candidates): return

            if sum_so_far < target:
                # 2 options: include, exclude
                seq.append(candidates[idx])
                # this subtree will contain at least 1+ instances of candidates[idx]
                solve(seq, idx, sum_so_far + candidates[idx])
                seq.pop()
                # this subtree will NOT contain any instances of candidates[idx]
                solve(seq, idx + 1, sum_so_far)
            elif sum_so_far == target:
                ret.append(list(seq))

        solve([], 0, 0)
        return ret

print(Solution().combinationSum([2, 3, 6, 7], 7))