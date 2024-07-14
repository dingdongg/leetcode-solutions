import math
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for t in tokens:
            if t.isnumeric() or (t[0] == '-' and len(t) > 1):
                operands.append(int(t))
            else:
                two = operands.pop()
                one = operands.pop()
                if t == "*": operands.append(one * two)
                elif t == "+": operands.append(one + two)
                elif t == "-": operands.append(one - two)
                elif t == "/":
                    # need to truncate twoards zero
                    res = one / two
                    if res > 0: operands.append(math.floor(res))
                    else: operands.append(math.ceil(res))

        return operands[0]
    
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))