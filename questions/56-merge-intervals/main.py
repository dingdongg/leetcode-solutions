from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals in non-decreasing order of start indexe
        intervals.sort(key=lambda i: i[0])
        START = 0
        END = 1
        ret = [intervals[0]]

        for i in range(1, len(intervals)):
            top = ret[-1]
            curr = intervals[i]
            
            if curr[START] > top[END]: ret.append(curr)
            else: ret[-1][END] = max(top[END], curr[END])
        
        return ret

s = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]

print(s.merge(intervals))