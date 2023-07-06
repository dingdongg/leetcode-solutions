from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        max_leng = 0
        l, r = 0, 0

        def most_freq():
            ret = 0
            for v in freq.values():
                ret = max(ret, v)
            return ret

        # length - most_freq <= k
        while r < len(s):
            char = s[r]
            freq[char] += 1
            leng = r - l + 1

            if leng - most_freq() <= k:
                max_leng = max(max_leng, leng)

            while (r - l + 1) - most_freq() > k:
                freq[s[l]] -= 1
                l += 1
            r += 1
        
        return max_leng
    
s = Solution()
print(s.characterReplacement("ABAB", 2))