from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:
                # move left bar to the right
                l += 1
            else:
                # if the 2 bars are equal height, it doesn't mattter
                # which bar you move (left or right).
                # this is because the height of all future potneital
                # areas will either be less than or equal to the current 
                # height (since both bars r equal)
                r -= 1
        
        return max_area
    
# height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
print(Solution().maxArea(height))