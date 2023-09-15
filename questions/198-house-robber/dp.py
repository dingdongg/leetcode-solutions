from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        self.nums = nums
        return self.solve(0)
    
    def solve(self, start_idx: int) -> int:
        if start_idx >= len(self.nums): return 0

        if start_idx + 2 not in self.memo:
            self.memo[start_idx + 2] = self.solve(start_idx + 2)
        if start_idx + 1 not in self.memo:
            self.memo[start_idx + 1] = self.solve(start_idx + 1)
        
        self.memo[start_idx] = max(
            self.nums[start_idx] + self.memo[start_idx + 2],
            self.memo[start_idx + 1],
        )

        return self.memo[start_idx]

s = Solution()
arr = [2,7,9,3,1]
print(s.rob(arr))