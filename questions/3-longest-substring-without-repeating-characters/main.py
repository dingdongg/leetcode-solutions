class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_size = 0
        chars = set()

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
                
            max_size = max(max_size, r - l + 1)
            chars.add(s[r])
            r += 1
        
        return max_size