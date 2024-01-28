class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def is_pali(s_l):
            for s in s_l:
                p_s, p_e = 0, len(s) - 1
                while p_s <= p_e:
                    if s[p_s] != s[p_e]:
                        return False
                    p_s += 1
                    p_e -= 1
            return True

        def dfs(i, part):
            if i == len(s):
                if is_pali(part):
                    answer.append(part.copy())
                return
            for j in range(i, len(s)):
                part.append(s[i : j + 1])
                dfs(j + 1, part)
                part.pop()

        dfs(0, [])
        return answer
