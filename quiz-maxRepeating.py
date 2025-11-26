class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        l, r = 1, len(sequence) // len(word)
        ans = -1
        highest_lps = [0]

        while l <= r:
            mid = (l + r) // 2
            wc = word * mid
            lps = highest_lps
            if len(wc) > len(highest_lps):
                i = len(highest_lps)
                _len = highest_lps[-1] if highest_lps else 0
                lps = highest_lps + [0] * (len(wc) - len(highest_lps))
                while i < len(wc):
                    # print("bruh", i, lps)
                    if wc[i] == wc[_len]:
                        _len += 1
                        lps[i] = _len
                        i += 1
                    else:
                        if _len == 0:
                            i += 1
                        else:
                            _len = lps[_len - 1]
                highest_lps = lps

            i = 0
            ptr_p = 0
            match = False
            while i < len(sequence):
                # print("bruh2", i, lps)
                if sequence[i] == wc[ptr_p]:
                    i += 1
                    ptr_p += 1
                    if ptr_p == len(wc):
                        match = True
                        break
                else:
                    if ptr_p == 0:
                        i += 1
                    else:
                        ptr_p = lps[ptr_p - 1]
            if match:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return 0 if ans == -1 else ans
