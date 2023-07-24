from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        ret = []
        
        if nums[r] > 0:
            sorted_nums = [] 

            while l <= r:
                left = nums[l] * nums[l]
                right = nums[r] * nums[r]

                to_append = max(left, right)
                sorted_nums.append(to_append)

                if left >= right or l == r: l += 1
                else: r -= 1
            
            # sorted_nums is now in non-increasing order
            for i in range(len(sorted_nums) - 1, -1, -1):
                ret.append(sorted_nums[i])
        else:
            for i in range(len(nums) -1, -1, -1):
                ret.append(nums[i] * nums[i])

        return ret
    

s = Solution()
print(s.sortedSquares([-4, -1, 0, 3, 10]))
