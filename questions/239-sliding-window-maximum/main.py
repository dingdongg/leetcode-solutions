from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0 # l, r pointers to keep track of window size
        ret = [] # return values
        q = deque() # monotonically decreasing queue (deque)

        # while our window is not at the end of the list,
        while r < len(nums):
            n = nums[r]
            # while our deque isn't empty and the top of the deque is 
            # less than our current number, pop them from the queue
            while q and n > q[-1]: q.pop()
            # append current number
            q.append(n)

            # if our window size is k,
            if r - l + 1 == k:
                # add the maximum value in our window to the ret list
                ret.append(q[0])
                # if the maximum value is where our left pointer is at, pop it from the queue
                if nums[l] == q[0]: q.popleft()
                l += 1 # increment left pointer
            r += 1 # increment right pointer
        
        return ret

s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
# print(s.maxSlidingWindow([1, -1], 1))