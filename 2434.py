from collections import deque


class Solution:
    def robotWithString(self, s: str) -> str:
        t = []
        ans = []
        s_idx = 0

        def op1():
            nonlocal s_idx
            t.append(s[s_idx])
            s_idx += 1

        def op2():
            ans.append(t.pop())

        smallest = "z"
        smallest_to_left = ["" for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            smallest = min(s[i], smallest)
            smallest_to_left[i] = smallest

        while s_idx != len(s) or t:
            if s_idx != len(s) and not t:
                op1()
            elif t and s_idx == len(s):
                op2()
            else:
                if smallest_to_left[s_idx] < t[-1]:
                    op1()
                else:
                    op2()

        return "".join(ans)
