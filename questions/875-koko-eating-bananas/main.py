from typing import List
import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h: return max(piles)

        slowest, fastest = 1, max(piles) + 1
        res = fastest

        while slowest < fastest:
            bph = (slowest + fastest) >> 1
            time_taken = 0
            for p in piles:
                time_taken += math.ceil(p / bph)

            if time_taken <= h:
                # can eat slower
                fastest = bph
                res = min(res, bph)
            elif time_taken > h:
                slowest = bph + 1

        return res

    
piles = [3, 6, 7, 11]
h = 8

print(Solution().minEatingSpeed(piles, h))
