from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            summed = numbers[l] + numbers[r]
            if summed > target:
                # shrink the current sum by decreemtning right pointer
                r -= 1
            elif summed < target:
                l += 1
            else:
                return [l + 1, r + 1]
            
s = Solution()
nums = [-1,0]
t = -1
print(s.twoSum(nums, t))