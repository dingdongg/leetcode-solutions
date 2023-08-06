class Solution:
    # def isHappy(self, n: int) -> bool:
    #     seen = set()

    #     _n = n
    #     while _n not in seen:
    #         seen.add(_n)
    #         _n = self.sum_digits_squared(_n)
    #         if _n == 1: return True
    #     return False

    def isHappy(self, n: int) -> bool:
        slow = fast = n

        while True:
            slow = self.sum_digits_squared(slow)
            fast = self.sum_digits_squared(
                self.sum_digits_squared(fast)
            )
            if slow == 1: return True
            if slow == fast: return False


    def sum_digits_squared(self, n: int) -> int:
        _n = n
        res = 0

        while _n != 0:
            digit = _n % 10
            res += digit ** 2
            _n //= 10
        
        return res