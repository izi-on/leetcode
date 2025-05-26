from functools import reduce


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        to_gain = list(
            filter(lambda x: x != 0, map(lambda x: max(0, (x ^ k) - x), nums))
        )
        to_lose = list(
            filter(lambda x: x != 0, map(lambda x: min(0, (x ^ k) - x), nums))
        )
        smallest_lost = max(to_lose) if to_lose else 0
        return (
            sum(to_gain) + sum(nums)
            if len(to_gain) % 2 == 0
            else sum(to_gain)
            - min(to_gain)
            + sum(nums)
            + max(0, (min(to_gain) + smallest_lost) if smallest_lost else 0)
        )
