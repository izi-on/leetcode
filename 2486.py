class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_curs = 0
        t_curs = 0
        while s_curs < len(s) and t_curs < len(t):
            if s[s_curs] == t[t_curs]:
                t_curs += 1
            s_curs += 1
        return len(t[t_curs:])
