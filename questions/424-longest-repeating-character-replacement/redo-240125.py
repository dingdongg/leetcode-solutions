from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        l, r = 0, 0

        def get_most_freq() -> int:
            ret = 0
            for v in freq.values():
                ret = max(ret, v)
            return ret

        max_len = 0
        while r < len(s):
            c = s[r]

            freq[c] += 1
            while (r - l + 1) - get_most_freq() > k:
                freq[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len

s = Solution()
print(s.characterReplacement("AABABBA", 1)) 


