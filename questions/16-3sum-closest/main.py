from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = float("infinity")
        prev = None

        for i, n in enumerate(nums):
            if n == prev: continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                curr_sum = n + nums[l] + nums[r]

                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum

                if curr_sum > target: r -= 1
                elif curr_sum < target:
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: l += 1
                else: return curr_sum

            prev = n
        
        return closest
    
s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1))
                
