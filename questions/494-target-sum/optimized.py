from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        res = self.solve(nums, 1, target, nums[0])
        return res if target != 0 else res * 2
    
    def solve(self, nums: List[int], start: int, target: int, curr: int) -> int:
        if (start, curr) in self.memo: return self.memo[(start, curr)]
        if len(nums) == start:
            return 1 if target == curr or target == curr * -1 else 0

        self.memo[(start, curr)] = self.solve(nums, start + 1, target, curr + nums[start]) + self.solve(nums, start + 1, target, curr - nums[start])

        return self.memo[(start, curr)]