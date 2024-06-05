from collections import defaultdict
from functools import reduce


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def redfunc(prev, x):
            x_dict = defaultdict(int)
            for c in x:
                x_dict[c] += 1
            remaining_keys = set(prev.keys()).intersection(set(x_dict.keys()))
            new_dict = {}
            for key in remaining_keys:
                new_dict[key] = min(prev[key], x_dict[key])
            return new_dict

        init = defaultdict(int)
        for c in words[0]:
            init[c] += 1
        letters_count = reduce(redfunc, words[1:], init)
        ans = []
        for letter, freq in letters_count.items():
            for _ in range(freq):
                ans.append(letter)
        return ans
