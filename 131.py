class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            if len(s) % 2 == 0:
                return s[: len(s) // 2] == s[len(s) // 2 :][::-1]
            else:
                return s[: len(s) // 2 + 1] == s[len(s) // 2 :][::-1]

        answer = []

        def helper(cur, idx):
            nonlocal answer
            if idx == len(s):
                answer.append(cur.copy())
                return
            for i in range(idx, len(s)):
                if not is_palindrome(s[idx : i + 1]):
                    continue
                cur.append(s[idx : i + 1])
                helper(cur, i + 1)
                cur.pop()

        helper([], 0)
        return answer
