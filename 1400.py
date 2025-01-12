from collections import defaultdict


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        char_freq = defaultdict(int)

        for c in s:
            char_freq[c] += 1

        odds = list(filter(lambda i: i[1] % 2 == 1, char_freq.items()))

        if len(odds) > k:
            return False

        max_amt = len(s)
        return max_amt >= k
