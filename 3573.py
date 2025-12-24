class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        mem = {}

        def helper(pidx, kl, state):
            if (pidx, kl, state) in mem:
                return mem[(pidx, kl, state)]

            if pidx == len(prices):
                return 0 if state != 2 else -float("inf")

            if kl == 0:
                return 0

            # option 1: skip transaction
            ans = helper(pidx + 1, kl, state)

            # option 2: do smthg
            if state == 0:
                ans = max(
                    ans,
                    -prices[pidx] + helper(pidx + 1, kl, 1),  # buy
                    prices[pidx] + helper(pidx + 1, kl, 2),  # sell
                )
            elif state == 1:  # holding a stock
                ans = max(
                    ans,
                    helper(pidx + 1, kl - 1, 0) + prices[pidx],  # sell the stock
                )
            elif state == 2:  # holding sell
                ans = max(
                    ans,
                    helper(pidx + 1, kl - 1, 0) - prices[pidx],  # buy the short shell
                )

            mem[(pidx, kl, state)] = ans
            return ans

        return helper(0, k, 0)
