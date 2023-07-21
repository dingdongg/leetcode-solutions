from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l, r = 0, 0
        word_leng = len(words[0])
        letters_perm = [0 for _ in range(26)]
        words_perm = defaultdict(int)
        letters_window = [0 for _ in range(26)]
        words_window = defaultdict(int)

        concat_str_leng = word_leng * len(words)
        ret = []

        for w in words:
            words_perm[w] += 1
            for c in w: 
                letters_perm[ord(c) - ord('a')] += 1

        while r < len(s):
            char = s[r]
            letters_window[ord(char) - ord('a')] += 1

            if (r - l + 1) == concat_str_leng:
                if letters_perm == letters_window:
                    for i in range(l, r + 1, word_leng):
                        key = s[i : i + word_leng]
                        words_window[key] += 1

                    if words_window == words_perm: ret.append(l)
                    words_window.clear()

                letters_window[ord(s[l]) - ord('a')] -= 1
                l += 1
            r += 1
        
        return ret

s = Solution()

words = ["foo", "bar"]
test = "barfoothefoobarman"

print(s.findSubstring(test, words))