from collections import defaultdict

class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_size = 0

        frequency = defaultdict(int)
        distinct_count = 0

        while r < len(s):
            if frequency[s[r]] == 0: distinct_count += 1
            frequency[s[r]] += 1

            if distinct_count <= k: max_size = max(max_size, r - l + 1)
            
            while distinct_count > k and (r - l + 1) > max_size:
                frequency[s[l]] -= 1
                if frequency[s[l]] == 0: distinct_count -= 1
                l += 1
            r += 1
        
        return max_size
    
s = Solution()
print(s.length_of_longest_substring_k_distinct("eceba", 3))
print(s.length_of_longest_substring_k_distinct("WORLD", 4))