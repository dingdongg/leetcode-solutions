from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_window_sum = nums[0] # maximum subarray that reaches up to the current index at any given iteration

        for i in range(1, len(nums)):
            next_num = nums[i]
            curr_window_sum = max(next_num, next_num + curr_window_sum)
            max_sum = max(max_sum, curr_window_sum)
        
        return max_sum


s = Solution()
test_list = [-2,1,-3,4,-1,2,1,-5,4]
test_ans = 6
print(f"{s.maxSubArray(test_list)};", f"expected: {test_ans}")