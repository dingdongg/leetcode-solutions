from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = set()
        unique_nums.add(nums[0])
        l, r = 0, 0

        while r < len(nums):
            n = nums[r]
            
            if n not in unique_nums:
                l += 1
                if r != l: nums[l] = nums[r]
                unique_nums.add(n)
                
            r += 1
        return len(unique_nums)
    
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))
print(nums)