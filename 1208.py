class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        s_p = 0
        max_len = 0
        cur_cost = 0
        for i in range(n):
            cur_cost += abs(ord(s[i]) - ord(t[i]))
            if cur_cost <= maxCost:
                max_len = i - s_p + 1
            else:
                cur_cost -= abs(ord(s[s_p]) - ord(t[s_p]))
                s_p += 1
        return max_len
