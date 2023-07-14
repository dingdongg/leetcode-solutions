from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        max_size = 0
        count = 0
        freq = defaultdict(int)

        while r < len(fruits):
            if freq[fruits[r]] == 0: count += 1
            freq[fruits[r]] += 1

            if count <= 2: max_size = max(max_size, r - l + 1)

            while count > 2 and (r - l + 1) > max_size:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0: count -= 1
                l += 1
                
            r += 1
        
        return max_size

s = Solution()
print(s.totalFruit([1,2,3,4,1,2,1,2])) # 4
        
