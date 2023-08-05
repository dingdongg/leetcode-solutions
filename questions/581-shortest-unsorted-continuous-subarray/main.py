from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[-1]
        start, end = -1, -1

        for i, n in enumerate(nums):
            if n < max_so_far: end = i
            max_so_far = max(max_so_far, n)
        
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > min_so_far: start = j
            min_so_far = min(min_so_far, nums[j])
        
        if start == -1: return 0
        return end - start + 1



    

s = Solution()
arr = [2, 6, 1, 8, 10, 9, 15]
# arr = [5,4,3,2,1]
print(s.findUnsortedSubarray(arr))