from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # smallest possible window in s such that all characters of t are included in it
        # (including duplicates)
        # CONSTRAINT: s and t only have upper/lower English letters (=52)

        s_freq = defaultdict(int) # frequency table of t
        t_freq = defaultdict(int) # frequency table of s

        # calculate t's frequency
        for char in t: t_freq[char] += 1

        # MAIN OPTIMIZATION, two variables used instead of a set to track the incomplete letters
        have, need = 0, len(t_freq) 

        # initialize pointers and return value
        l, r = 0, 0
        pointers = (0, len(s))

        # sliding window loop
        while r < len(s):
            char = s[r]
            # if char is one of the letters in t, add it to s_freq and increment
            if char in t_freq: 
                s_freq[char] += 1 

                # if we now have enough of the letter we're looking for,
                if s_freq[char] == t_freq[char]:
                    have += 1 # increment the number of letters satisfied

                    # while we have a substring that has all the characters of t,
                    while have == need:
                        # update min_leng pointers
                        if (r - l + 1) < (pointers[1] - pointers[0] + 1): pointers = (l, r)
                        # if the left pointer letter is in s/t,
                        if s[l] in s_freq: 
                            # decrement its frequency
                            s_freq[s[l]] -= 1
                            # if we now have less than what we need, decrement the number of letters satisfied
                            if s_freq[s[l]] < t_freq[s[l]]: have -= 1
                        l += 1 # increment left pointer
            r += 1 # increment right pointer

        if (pointers[1] - pointers[0] + 1) > len(s): return "" # no valid window edge case
        return s[pointers[0]:pointers[1] + 1]
    
s = Solution()

print(s.minWindow("ADOBECODEBANC", "ABC"))




