from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)
        num_done = 0
        
        for i in range(len(s1)): s1_freq[s1[i]] += 1
        num_need = len(s1_freq)

        while r < len(s2):
            char = s2[r]
            if char in s1_freq:
                s2_freq[char] += 1
                if s2_freq[char] == s1_freq[char]: num_done += 1
            
            if num_done == num_need and len(s1) == (r - l + 1): return True

            while (r - l + 1) >= len(s1):
                to_remove = s2[l]
                if to_remove in s1_freq:
                    if s1_freq[to_remove] == s2_freq[to_remove]: num_done -= 1
                    s2_freq[to_remove] -= 1
                l += 1
            r += 1
        
        return False


s = Solution()
print(s.checkInclusion(
    "trinitrophenylmethylnitramine",
    "dinitrophenylhydrazinetrinitrophenylmethylnitramine"
))