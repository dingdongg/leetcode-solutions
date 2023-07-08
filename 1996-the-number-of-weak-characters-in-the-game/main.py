from typing import List

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        weakCharacters = 0 # count
        maxDefense = 0 # largest defense so far

        # sorted in descending attack order, then ascending defense order 
        # O(n log n)
        properties.sort(key = lambda x: (-x[0], x[1]))

        # for each character,
        for _, defense in properties:
            # if its defense is lower than the max def so far,
            # it must be weaker (since attack is in descending order)
            if defense < maxDefense: weakCharacters += 1
            # otherwise, update the max defense
            else: maxDefense = defense

        return weakCharacters
    
s = Solution()
val = [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]
print(s.numberOfWeakCharacters(val))