from typing import (
    List,
)
# from lintcode import (
#     Interval,
# )

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        starts = list(map(lambda x: x.start, sorted(intervals, key=lambda i: i.start)))
        ends = list(map(lambda x: x.end, sorted(intervals, key=lambda i: i.end)))

        i = j = 0
        max_so_far = -1
        rooms = 0

        while i < len(starts) and j < len(ends):
            rooms += -1 if ends[j] <= starts[i] else 1
            if ends[j] <= starts[i]: j += 1
            else:
                max_so_far = max(max_so_far, rooms)
                i += 1
        
        return max_so_far

            
                

s = Solution()
intervals = [Interval(0,30),Interval(5,10),Interval(15,20)]
print(s.min_meeting_rooms(intervals))


