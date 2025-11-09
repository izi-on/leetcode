class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        cum = []
        cur_sum = 0
        for s in stations:
            cur_sum += s
            cum.append(cur_sum)
        cum.append(0)

        tstations = []
        for i in range(n):
            prev_t = cum[max(0, i - r) - 1]
            next_t = cum[min(i + r, n - 1)]
            tstations.append(next_t - prev_t)

        def possible(x):
            tst = [0] * n
            cur_sum = 0
            used = 0
            for i in range(n):
                if i - r - 1 >= 0:
                    cur_sum -= tst[i - r - 1]
                need = max(0, x - tstations[i] - cur_sum)
                used += need
                cur_sum += need
                tst[min(n - 1, i + r)] = need
                if used > k:
                    return False
            return True

        min_x = 0
        max_x = sum(stations) + k
        ans = -1
        while min_x <= max_x:
            mid = (min_x + max_x) // 2
            if possible(mid):
                ans = mid
                min_x = mid + 1
            else:
                max_x = mid - 1
        return ans
