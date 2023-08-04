from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        l, r = 0, 0
        count = 0
        prod = 1

        while r < len(nums):
            prod *= nums[r]

            while prod >= k:
                prod /= nums[l]
                l += 1
            
            count += (r - l + 1)
            r += 1
        
        return count
    

s = Solution()

test_arr = [57,44,92,28,66,60,37,33,52,38,29,76,8,75,22]
k = 18

print(s.numSubarrayProductLessThanK(test_arr, k))