class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_processed = self.process(s)
        t_processed = self.process(t)

        return t_processed == s_processed
    
    def process(self, s: str) -> str:
        ptr = len(s) - 1
        backspaces = 0
        res = ""

        while ptr > -1:
            if s[ptr] == "#": backspaces += 1
            else:
                if backspaces > 0: backspaces -= 1
                else: res += s[ptr]
            ptr -= 1

        return res

s = Solution()

print(s.backspaceCompare("ab#d", "ac#d"))