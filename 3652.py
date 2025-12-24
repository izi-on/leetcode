class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        prefix = [0]
        for i in range(n):
            prefix.append(prices[i] * strategy[i] + prefix[-1])

        sell_pref = [0]
        for i in range(n):
            sell_pref.append(prices[i] + sell_pref[-1])

        ans = prefix[-1]
        for i in range(k - 1, n):
            cur_sum = (
                prefix[-1]
                - prefix[i + 1]
                + prefix[i - k + 1]
                + sell_pref[i + 1]
                - sell_pref[i - k // 2 + 1]
            )
            ans = max(ans, cur_sum)
        return ans
