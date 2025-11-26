class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        na = len(a)
        nb = len(b)
        at = a * max(2, ((2 * (nb) + na - 1) // na))  # max amt of reps

        i = 1
        n = len(b)
        lps = [0] * n
        _len = 0
        while i < n:
            if b[i] == b[_len]:
                _len += 1
                lps[i] = _len
                i += 1
            else:
                if _len == 0:
                    i += 1
                else:
                    _len = lps[_len - 1]

        i = 0
        ptr_p = 0
        m = len(at)
        ans = -1
        while i < m:
            if at[i] == b[ptr_p]:
                ptr_p += 1
                i += 1
                if ptr_p == len(b):
                    ans = i
                    break
            else:
                if ptr_p == 0:
                    i += 1
                else:
                    ptr_p = lps[ptr_p - 1]

        if ans == -1:
            return -1
        return (ans + na - 1) // na
