from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = self.solve(nums, 1, target, nums[0])
        return res if target != 0 else res * 2
    
    def solve(self, nums: List[int], start: int, target: int, curr: int) -> int:
        if len(nums) == start:
            return 1 if target == curr else 0

        return self.solve(nums, start + 1, target, curr + nums[start]) + self.solve(nums, start + 1, target, curr - nums[start])

            

s = Solution()
arr = [1,5,3,2,2]
t = 9
print(s.findTargetSumWays(arr, t))