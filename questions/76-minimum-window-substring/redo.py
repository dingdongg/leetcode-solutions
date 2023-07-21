from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0 
        min_window = [-1, len(s) + 1]

        t_freq = defaultdict(int)
        s_freq = defaultdict(int)

        for char in t: t_freq[char] += 1
        need = len(t_freq.keys())
        have = 0

        while r < len(s):
            char = s[r]
            s_freq[char] += 1

            if char in t_freq and s_freq[char] == t_freq[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < min_window[1]: min_window = [l, (r - l + 1)]

                s_freq[s[l]] -= 1
                if s[l] in t_freq and s_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
            r += 1
        
        if min_window[0] == -1: return ""
        return s[min_window[0]:min_window[0] + min_window[1]]

s = Solution()
print(s.minWindow("aab", "aab"))

