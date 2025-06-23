class Solution:
    # (freq_a - left_a) - (freq_b - left_b)
    # = (freq_a - freq_b) - (left_a - left_b) (minimize right side)
    def maxDifference(self, s: str, k: int) -> int:
        ans = -float("inf")
        for c1 in "01234":
            for c2 in "01234":
                if c1 == c2:
                    continue

                best = [float("inf") for _ in range(4)]

                freq_c1 = 0
                freq_c2 = 0
                freq_l_c1 = 0
                freq_l_c2 = 0
                left = -1
                for right, chr_r in enumerate(s):
                    if chr_r == c1:
                        freq_c1 += 1
                    elif chr_r == c2:
                        freq_c2 += 1

                    while (right - left) >= k and freq_l_c2 >= 2:
                        status = ((freq_l_c1 % 2) * 2) & (freq_l_c2 % 2)
                        best[status] = min(best[status], freq_l_c1 - freq_l_c2)

                        left += 1
                        ch_l = s[left]
                        if ch_l == c1:
                            freq_l_c1 += 1
                        elif ch_l == c2:
                            freq_l_c2 += 1
                    status_needed = (((freq_c1 % 2) * 2) & (freq_c2 % 2)) ^ 0b10
                    ans = max(ans, freq_c1 - freq_c2 - best[status_needed])
                    print(ans, freq_c1, freq_c2, best[status_needed])
        return ans
