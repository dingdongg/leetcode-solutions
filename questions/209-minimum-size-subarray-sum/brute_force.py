from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums) + 1

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum >= target: size = min(size, j - i + 1)

        return size if size != len(nums) + 1 else 0

s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
