class Solution:
    def minimumLength(self, s: str) -> int:
        char_freq = {}
        for c in s:
            char_freq[c] = char_freq.get(c, 0) + 1
        count = 0
        for val in char_freq.values():
            if val % 2 == 1:
                count += 1
            elif val % 2 == 0:
                count += 2
        return count
