from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # smallest possible window in s such that all characters of t are included in it
        # (including duplicates)
        # CONSTRAINT: s and t only have upper/lower English letters (=52)

        s_freq = defaultdict(int) # frequency table of t
        t_freq = defaultdict(int) # frequency table of s

        # used to check which elements have yet to be fully included in the min. window
        incomplete = set() 

        # calculate t's frequency, add letters to check for into the set
        for char in t:
            t_freq[char] += 1
            incomplete.add(char)

        # initialize pointers and return value
        l, r = 0, 0
        pointers = (0, len(s))

        # sliding window loop
        while r < len(s):
            char = s[r]
            # if char is one of the chars to look for, add it to s_freq and increment
            if char in t_freq: s_freq[char] += 1 
            
            # if char is one of the chars to look for and we have enough of the chars in the window:
            if char in incomplete and s_freq[char] >= t_freq[char]:
                # remove it from the chars to look for
                incomplete.remove(char)

                # while we have no more chars to look for, 
                while len(incomplete) == 0:
                    # update return value (pointers that make up min. window)
                    if (r - l + 1) < (pointers[1] - pointers[0] + 1):
                        pointers = (l, r)
                    # if left pointer char is one of the chars in t,
                    if s[l] in s_freq: 
                        # decrement frequency
                        s_freq[s[l]] -= 1
                        # if we have less of the char we need, add it to the set of incompletes
                        if s_freq[s[l]] < t_freq[s[l]]: incomplete.add(s[l])
                    l += 1 # increment left pointer
            r += 1 # increment right pointer

        if (pointers[1] - pointers[0] + 1) > len(s): return "" # no valid window edge case
        return s[pointers[0]:pointers[1] + 1]
    
s = Solution()

print(s.minWindow("a", "a"))




