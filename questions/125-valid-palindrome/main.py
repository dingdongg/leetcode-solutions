class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1
            if l >= r: break

            left, right = s[l], s[r]

            if s[l].isalpha() and s[r].isalpha():
                ordl, ordr = ord(s[l]), ord(s[r])
                threshold = ord('a')
                if ordl < threshold: left = chr(ordl + 32)
                if ordr < threshold: right = chr(ordr + 32)

            if left != right: return False
            l += 1
            r -= 1
        
        return True

test = "A man, a plan, a canal: Panama"

print(Solution().isPalindrome(test))