class MinStack:
    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))

    def pop(self) -> None:
        self.data.pop()
        self.mins.pop()
        
    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        
cmd = ["MinStack","push","push","push","getMin","pop","top","getMin"]
args = [[],[-2],[0],[-3],[],[],[],[]]

s = None

for i in range(len(cmd)):
    c, a = cmd[i], args[i]
    if c == "MinStack":
        s = MinStack()
    elif c == "push":
        s.push(a)
        print(f"pushed {a[0]}")
    elif c == "getMin":
        res = s.getMin()
        print(f"getMin() = {res}")
    elif c == "pop":
        res = s.pop()
        print(f"pop() = {res}")
    elif c == "top":
        res = s.top()
        print(f"top() = {res}")

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()