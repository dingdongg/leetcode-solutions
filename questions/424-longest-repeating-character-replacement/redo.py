from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_size = 0
        freq = defaultdict(int)

        def get_max_freq() -> int:
            max_so_far = -1
            for k in freq.keys():
                max_so_far = max(max_so_far, freq[k])
            return max_so_far
        
        while r < len(s):
            char = s[r]
            freq[char] += 1

            length = r - l + 1
            if (length - get_max_freq()) <= k:
                max_size = max(max_size, length)
                r += 1
                continue 
            
            while length - get_max_freq() > k and length > max_size:
                freq[s[l]] -= 1
                if freq[s[l]] == 0: del freq[s[l]]
                l += 1
                length = r - l + 1
            r += 1
        
        return max_size
    
s = Solution()
print(s.characterReplacement("AABABBA", 1))