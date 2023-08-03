from typing import List

class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     color_freq = [0, 0, 0]

    #     for color in nums: color_freq[color] += 1

    #     start = 0
    #     for j in range(0, len(color_freq)):
    #         for i in range(start, start + color_freq[j]):
    #             nums[i] = j
    #         start += color_freq[j]

    def sortColors(self, nums: List[int]) -> None:
        start = 0
        for color in range(0, 3):
            for right in range(start, len(nums)):
                if nums[right] == color:
                    temp = nums[right]
                    nums[right] = nums[start]
                    nums[start] = temp
                    start += 1

s = Solution()
arr = [2, 0, 2, 1, 1, 0]
s.sortColors(arr)
print(arr)