from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START = 0
        END = 1
        i = 0
        ret = []
        insert_pos = 0

        while i < len(intervals):
            curr = intervals[i]
            if curr[END] < newInterval[START] or curr[START] > newInterval[END]:
                ret.append(curr)
                if curr[END] < newInterval[START]: insert_pos += 1
                i += 1
            else:
                merged = [min(intervals[i][START], newInterval[START]), newInterval[END]]
                while i < len(intervals) and intervals[i][START] <= newInterval[END]:
                    merged[END] = max(merged[END], intervals[i][END])
                    i += 1
                ret.append(merged)
                return ret + intervals[i:]
        
        return ret[0:insert_pos] + [newInterval] + ret[insert_pos:]
    

s = Solution()

intervals = [[3,5],[12,15]]
newInterval = [6,6]

print(s.insert(intervals, newInterval))