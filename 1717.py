from collections import deque


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        new_str = deque()
        h_p = "ab" if x > y else "ba"
        for i in range(len(s)):
            if s[i] == h_p[1] and new_str and new_str[-1] == h_p[0]:
                new_str.pop()
            else:
                new_str.append(s[i])
        answer = (len(s) - len(new_str)) * max(x, y) // 2

        l_p = "ab" if x <= y else "ba"
        s = "".join(list(new_str))
        new_str = deque()
        for i in range(len(s)):
            if s[i] == l_p[1] and new_str and new_str[-1] == l_p[0]:
                new_str.pop()
            else:
                new_str.append(s[i])
        answer += (len(s) - len(new_str)) * min(x, y) // 2
        return answer
