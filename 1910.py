from collections import deque


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        def build_lps(part):
            lps = [0] * len(part)
            i = 1
            j = 0
            while i < len(part):
                if part[j] == part[i]:
                    j += 1
                    lps[i] = j
                    i += 1
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = build_lps(part)
        j = 0
        i = 0
        stack = deque()
        while i < len(s):
            if s[i] == part[j]:  # char match
                stack.append((s[i], j + 1))
                j += 1
                i += 1
                # check if full match
                if j == len(part):
                    for _ in range(len(part)):
                        stack.pop()
                    j = stack[-1][1] if stack else 0
            else:
                stack.append((s[i], j))
                if j != 0:
                    j = lps[j - 1]
                    stack.pop()
                else:
                    i += 1

        return "".join(list(map(lambda x: x[0], stack)))
