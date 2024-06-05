from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        max_length = 0
        remainder = 0
        for _, val in count.items():
            if val % 2 == 1:
                remainder = 1
            max_length += val - val % 2
        return max_length + remainder
