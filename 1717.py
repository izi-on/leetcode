class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        q = deque()
        priority = "ab" if x > y else "ba"
        priority2 = "ba" if x > y else "ab"
        p1 = x if x > y else y
        p2 = y if x > y else x
        ans = 0
        for c in s:
            q.append(c)
            if len(q) >= 2:
                comp = q[-1] + q[-2]
                if comp == priority:
                    q.pop()
                    q.pop()
                    ans += p1
        q2 = deque()
        for c in q:
            q2.append(c)
            if len(q2) >= 2:
                comp = q2[-1] + q2[-2]
                if comp == priority2:
                    q2.pop()
                    q2.pop()
                    ans += p2
        return ans
