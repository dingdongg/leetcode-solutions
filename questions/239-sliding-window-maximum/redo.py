from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        q = deque() # decreasing queue of indexes
        r = 0

        while r < len(nums):
            while q and q[0] < (r - k + 1):
                q.popleft()
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if (r - k + 1) >= 0: maxes.append(nums[q[0]])
            r += 1
        
        return maxes
    
nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(Solution().maxSlidingWindow(nums, k))