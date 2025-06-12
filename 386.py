from collections import deque


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = deque()

        def helper(cur: int):
            nonlocal ans

            if cur > n:
                return
            ans.append(cur)

            cur *= 10
            for c in range(10):
                cur_c = cur + c
                helper(cur_c)

        for c in range(1, 10):
            helper(c)
        return list(ans)
