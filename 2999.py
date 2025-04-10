class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        finish_str = str(finish)
        start_str = str(start)
        n = len(finish_str)
        start_str = start_str.zfill(n)
        prefix_len = n - len(s)

        @cache
        def digit_dp(i, low_limit, high_limit):
            if i == n:
                return 1

            res = 0
            lo = int(start_str[i]) if low_limit else 0
            hi = int(finish_str[i]) if high_limit else 9
            if i < prefix_len:
                for j in range(lo, min(hi, limit) + 1):
                    res += digit_dp(
                        i + 1, low_limit and j == lo, high_limit and j == hi
                    )
            else:
                cur_s = int(s[i - prefix_len])
                if lo <= cur_s <= min(limit, hi):
                    res = digit_dp(
                        i + 1, low_limit and cur_s == lo, high_limit and cur_s == hi
                    )
                else:
                    res = 0
            return res

        return digit_dp(0, True, True)
