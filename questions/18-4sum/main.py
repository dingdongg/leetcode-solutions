from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        prev = None

        for i, n in enumerate(nums):
            if n == prev: continue

            triplets = self.threeSum(nums, target - n, i + 1)
            for t in triplets: res.append(t + [n])
            
            prev = n
        return res

    
    def threeSum(self, nums: List[int], target: int, start: int) -> List[List[int]]:
        res = []
        prev = None

        for i in range(start, len(nums)):
            n = nums[i]
            if n == prev: continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                triplet_sum = n + nums[l] + nums[r]

                if triplet_sum > target:
                    r -= 1
                elif triplet_sum < target:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])

                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
            prev = n
        return res


s = Solution()
arr = [1, 0, -1, 0, -2, 2]
target = 0
# print(s.threeSum(arr, target, 0))
print(s.fourSum(arr, target))