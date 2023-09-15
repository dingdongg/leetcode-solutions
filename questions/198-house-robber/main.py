from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        return self.solve(0)
    
    def solve(self, start_idx: int) -> int:
        if start_idx >= len(self.nums): return 0

        return max(
            self.nums[start_idx] + self.solve(start_idx + 2),
            self.solve(start_idx + 1),
        )

s = Solution()
arr = [2,7,9,3,1]
print(s.rob(arr))