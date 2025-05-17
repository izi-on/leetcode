from functools import reduce
from collections import defaultdict


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        freq = defaultdict(int)
        for c in s:
            freq[ord(c) - ord("a")] += 1

        for _ in range(t):
            new_freq = defaultdict(int)
            for i in range(26):
                replace_ahead = nums[i]
                for j in range(i + 1, i + replace_ahead + 1):
                    new_freq[j % 26] += freq[i] % (10**9 + 7)
            freq = new_freq

        return reduce(lambda acc, x: (acc + x) % (10**9 + 7), freq.values(), 0)
