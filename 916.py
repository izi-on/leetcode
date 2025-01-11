from functools import reduce
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        char_freq_l = map(
            lambda word: reduce(lambda acc, v: {**acc, v: acc.get(v, 0) + 1}, word, {}),
            words2,
        )

        min_char_freq = {}
        for d in char_freq_l:
            for c, count in d.items():
                if c not in min_char_freq.keys():
                    min_char_freq[c] = count
                    continue
                min_char_freq[c] = max(min_char_freq[c], count)

        def filt(word):
            word_freq = reduce(lambda acc, x: {**acc, x: acc.get(x, 0) + 1}, word, {})
            for char, count in min_char_freq.items():
                if not (count <= word_freq.get(char, 0)):
                    return False
            return True

        return list(filter(filt, words1))
