from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-infinity")

        # check out the sum of every subarray, starting at index i  
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)
        
        return max_sum
    
s = Solution()
test_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(test_list))