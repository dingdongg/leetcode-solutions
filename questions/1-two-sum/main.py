from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}

        for i, n in enumerate(nums):
            if n in need: return [i, need[n]]

            need[target - n] = i
        
        return [-1, -1]
    
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))