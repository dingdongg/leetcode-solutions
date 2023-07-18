from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, 0
        p_freq = defaultdict(int) # O(26)
        s_freq = defaultdict(int) # O(26)
        ret = []

        for c in p: p_freq[c] += 1

        while r < len(s):
            char = s[r]
            s_freq[char] += 1

            # we found a permutation
            if s_freq == p_freq: ret.append(l)
            
            while (r - l + 1) >= len(p):
                s_freq[s[l]] -= 1
                if s_freq[s[l]] == 0: del s_freq[s[l]]
                l += 1
            r += 1
        
        return ret
    
s = Solution()
print(s.findAnagrams("abab", "ab"))