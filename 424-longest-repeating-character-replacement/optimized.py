from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        max_leng = 0
        l, r = 0, 0
        max_freq = 0

        # length - most_freq <= k
        while r < len(s):
            char = s[r]
            freq[char] += 1
            max_freq = max(max_freq, freq[char])
            leng = r - l + 1

            if leng - max_freq <= k:
                max_leng = max(max_leng, leng)

            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            r += 1
        
        return max_leng
    
s = Solution()
print(s.characterReplacement("AABABBA", 2))