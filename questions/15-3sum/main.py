from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        prev = None

        for i, n in enumerate(nums):
            if n == prev: continue

            l, r = i + 1, len(nums) - 1
            target = -n

            while l < r:
                curSum = nums[l] + nums[r]
                if curSum > target: r -= 1
                elif curSum < target: l += 1
                else: 
                    ret.append([n, nums[l], nums[r]])
                    # l += 1
                    # while nums[l] == nums[l - 1] and l < r:
                    #     l += 1
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
            
            prev = n
        
        return ret
    
s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))