class MinStack:
    def __init__(self):
        self.stack = []  # [(val, cur_min)]

    def push(self, val: int) -> None:
        cur_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    s = MinStack()
    s.push(1)
    s.push(2)
    print(s.top())  # Output: 2
    print(s.getMin())  # Output: 1
    s.pop()
    print(s.top())  # Output: 1
    print(s.getMin())  # Output: 1
