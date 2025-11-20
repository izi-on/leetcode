class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def _pop(self, keep):
        if not self.s2:
            while self.s1:
                p = self.s1.pop()
                self.s2.append(p)
        if keep:
            return self.s2[-1]
        return self.s2.pop()

    def pop(self) -> int:
        return self._pop(False)

    def peek(self) -> int:
        return self._pop(True)

    def empty(self) -> bool:
        return (not self.s1) and (not self.s2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
