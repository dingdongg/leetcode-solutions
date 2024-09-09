from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        valid_combos = {} # tuple -> list[int]
        seq = [] # stack that keeps track of our DFS progress

        def dfs(idx: int, curr_sum: int):
            print(f"idx: {idx}, curr_sum: {curr_sum}")
            if curr_sum < target:
                # we need to recurse with an additional element added in our seq
                for k in range(idx, len(candidates)):
                    seq.append(candidates[k])
                    dfs(k, curr_sum + candidates[k])
                    seq.pop()
            elif curr_sum == target:
                # seqwuence works, add to valid_combos
                # compute tuple key and use that to add it
                freq = [0] * 41
                for num in seq:
                    freq[num] += 1
                key = tuple(freq)
                if key not in valid_combos: 
                    valid_combos[key] = list(seq)
            # curr_sum > target; this sequence doesn't work. just exit.

        dfs(0, 0)
    
        ret = []
        for v in valid_combos.values():
            ret.append(v)
        
        return ret
    


candidates = [2,3,6,7]
target = 7

print(Solution().combinationSum(candidates, target))