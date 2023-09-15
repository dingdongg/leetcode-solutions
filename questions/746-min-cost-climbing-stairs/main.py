from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.solve(0, cost), self.solve(1, cost))

    def solve(self, start_idx: int, cost: List[int]) -> int:
        if start_idx >= len(cost): return 0

        return cost[start_idx] + min(self.memo[start_idx + 1], self.memo[start_idx + 2])


s = Solution()
arr = [10,15,20]
print(s.minCostClimbingStairs(arr))