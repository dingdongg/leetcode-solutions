from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_duplicate = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]: 
                nums[next_duplicate] = nums[r]
                next_duplicate += 1
        
        return next_duplicate
    
s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.removeDuplicates(nums))
print(nums)