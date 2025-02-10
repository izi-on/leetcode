from collections import deque


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = deque()

        for c in s:
            if not c.isdigit():
                stack.append(c)
            else:
                stack.pop()

        return "".join(list(stack))
