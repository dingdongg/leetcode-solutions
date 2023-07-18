from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        max_size = 0
        zero_freq = 0

        while r < len(nums):
            if nums[r] == 0: zero_freq += 1

            if zero_freq <= k: max_size = max(max_size, r - l + 1)

            while zero_freq > k and (r - l + 1) > max_size:
                if nums[l] == 0: zero_freq -= 1
                l += 1
            r += 1
        
        return max_size
    

s = Solution()
test_arr = [1,1,1,0,0,0,1,1,1,1,0]
test_k = 2
print(s.longestOnes(test_arr, test_k))