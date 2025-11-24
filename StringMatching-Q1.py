class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        _len = 0
        n = len(s)
        lps = [0] * n
        lps[0] = 0
        i = 1
        while i < n:
            if s[i] == s[_len]:
                _len += 1
                lps[i] = _len
                i += 1
            else:
                if _len == 0:
                    lps[i] = 0
                    i += 1
                else:
                    _len = lps[_len - 1]

        ptr_p = 0
        t = (s + s)[1:-1]
        m = len(t)
        i = 0
        while i < m:
            if t[i] == s[ptr_p]:
                i += 1
                ptr_p += 1
            else:
                if ptr_p == 0:
                    i += 1
                else:
                    ptr_p = lps[ptr_p - 1]
            if ptr_p == len(s):
                return True
        return False
