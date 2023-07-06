from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        # return true if one of the permutations of s1 is a substring of s2
        # CONSTRAINT: s1 and s2 consist of ONLY lowercase english characters (=26)
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)

        for s in s1: s1_freq[s] += 1

        l, r = 0, 0

        while r < len(s2):
            char = s2[r]
            s2_freq[char] += 1
            leng = r - l + 1

            if leng > len(s1):
                # slide left window
                s2_freq[s2[l]] -= 1
                if s2_freq[s2[l]] == 0: del s2_freq[s2[l]]
                l += 1
            
            if s1_freq == s2_freq: return True

            r += 1
        
        return False
    
s = Solution()
print(s.checkInclusion("ab", "eidboaooo"))
