from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList: return []

        ret = []
        i = j = 0
        START = 0
        END = 1

        while i < len(firstList) and j < len(secondList):
            first, second = firstList[i], secondList[j]
            is_earlier_first = first[START] <= second[START]
            earlier_interval = first if is_earlier_first else second
            later_interval = second if is_earlier_first else first
            later_ends_first = later_interval[END] <= earlier_interval[END]

            if earlier_interval[END] >= later_interval[START]: 
                ret.append([
                    max(later_interval[START], earlier_interval[START]),
                    min(later_interval[END], earlier_interval[END]),
                ])

            if is_earlier_first:
                if later_ends_first: j += 1 
                else: i += 1
            else:
                if later_ends_first: i += 1
                else: j += 1

        return ret
    
s = Solution()

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

print(s.intervalIntersection(firstList, secondList))