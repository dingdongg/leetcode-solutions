class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dynamic size window
        # contiguous data
        # = sliding window technique
        l, r = 0, 0
        seen = set()
        length = 0

        while r < len(s):
            while s[r] in seen and l < r:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            length = max(length, r - l + 1)
            r += 1

        return length
    

s = 'abcabcbb'
print(Solution().lengthOfLongestSubstring(s))