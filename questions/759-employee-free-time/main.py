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

    def __str__(self):
        return f"({self.start}, {self.end})"

    def __repr__(self):
        return self.__str__()

class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        # Write your code here
        starts = []
        ends = []

        for employee in schedule:
            for i in range(1, len(employee), 2):
                starts.append(employee[i - 1])
                ends.append(employee[i])
        
        starts.sort()
        ends.sort()

        ret = []
        occupied = 0
        s = e = 0

        while s < len(starts) and e < len(ends):
            if starts[s] <= ends[e]:
                occupied += 1
                s += 1
            else:
                occupied -= 1
                if occupied == 0:
                    ret.append(Interval(ends[e], starts[s]))
                e += 1
        
        return ret
    

s = Solution()
schedule = [[1,3,6,7],[2,4],[2,5,9,12]]
print(s.employee_free_time(schedule))