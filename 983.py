class Solution:
    def find_prev_subp_idx(self, target, days):
        l, r = 0, len(days) - 1
        ans = -1
        while l <= r:
            print(l, r, ans)
            mid = (l + r) // 2
            if days[mid] < target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        map_idx_to_dur = {0: 0, 1: 6, 2: 29}
        dp: list[float | int] = [-1] * len(days)
        for i in range(len(dp)):
            min_cost: int | float = float("inf")
            for j in range(len(costs)):
                cur_day = days[i]
                to_add = 0
                prev = self.find_prev_subp_idx(cur_day - map_idx_to_dur[j], days)
                # print(prev, cur_day - map_idx_to_dur[j])
                if prev != -1:
                    to_add = dp[prev]
                cost = costs[j] + to_add
                min_cost = min(cost, min_cost)
            dp[i] = min_cost
            # print(dp)
        return dp[-1]
