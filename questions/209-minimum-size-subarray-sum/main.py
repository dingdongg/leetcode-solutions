from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0 
        size = len(nums) + 1
        curr_sum = 0

        while r < len(nums):
            curr_sum += nums[r]

            while curr_sum >= target:
                size = min(r - l + 1, size)
                curr_sum -= nums[l]
                l += 1
            r += 1

        return size if size != len(nums) + 1 else 0

s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
