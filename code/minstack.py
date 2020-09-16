import collections

class MinStack:

    def __init__(self):
        self.stack = collections.deque()
        self.min=0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min= min(self.min,x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.push(1)
obj.push(12)
obj.push(0)
param_3 = obj.top()
obj.pop()
obj.push(-1)
param_4 = obj.getMin()
print( str(param_3) + str(param_4))
