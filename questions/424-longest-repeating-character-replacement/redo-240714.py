class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        leng = 0
        count = [0] * 26 # uppercase letters only
        max_freq = 0

        while r < len(s):
            idx = ord(s[r]) - ord('A')
            count[idx] += 1
            max_freq = max(max_freq, count[idx])
            while (r - l + 1) - max_freq > k and l < r:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            leng = max(leng, r - l + 1)
            r += 1
        
        return leng

s = "AABABBA"
k = 1

print(Solution().characterReplacement(s, k))