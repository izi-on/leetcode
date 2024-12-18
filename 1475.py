from collections import deque


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        map_to_discount = {}
        stack = deque()
        for i, price in enumerate(prices):
            while stack and price <= stack[-1][1]:
                map_to_discount[stack[-1][0]] = price
                stack.pop()
            stack.append((i, price))
        ans = [-1] * len(prices)
        for i in range(len(ans)):
            ans[i] = prices[i] - map_to_discount.get(i, 0)
        return ans
