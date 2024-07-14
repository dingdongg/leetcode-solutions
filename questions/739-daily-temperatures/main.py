from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]
            
            while stack and stack[-1][1] < t:
                colder_day = stack.pop()
                res[colder_day[0]] = i - colder_day[0]
            stack.append([i, t])
        
        return res
    

Solution().dailyTemperatures([73,74,75,71,69,72,76,73])