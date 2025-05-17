from collections import defaultdict
from functools import reduce


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = defaultdict(int)
        for c in s:
            a_idx = ord(c) - ord("a")
            freq[a_idx] += 1

        for _ in range(t):
            freq[0] = freq[25]
            freq[1] = freq[0] + freq[25] % (10**9 + 7)
            for i in range(2, 26):
                freq[i] = freq[i - 1]

        return reduce(lambda x, v: x + v % (10**9 + 7), freq.values(), 0)
