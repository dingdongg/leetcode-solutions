from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}
        return min(self.solve(0, cost), self.solve(1, cost))

    def solve(self, start_idx: int, cost: List[int]) -> int:
        if start_idx >= len(cost): return 0

        if start_idx + 1 not in self.memo: 
            self.memo[start_idx + 1] = self.solve(start_idx + 1, cost)
        if start_idx + 2 not in self.memo: 
            self.memo[start_idx + 2] = self.solve(start_idx + 2, cost)

        self.memo[start_idx] = cost[start_idx] + min(self.memo[start_idx + 1], self.memo[start_idx + 2])
        return self.memo[start_idx]


s = Solution()
arr = [10,15,20]
print(s.minCostClimbingStairs(arr))