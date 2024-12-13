from collections import defaultdict
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        adj_list = defaultdict(lambda: set())
        for i, _ in enumerate(nums):
            adj_list[i] = set([max(i - 1, 0), min(i + 1, len(nums) - 1), i])
        marked = set()
        nt = sorted(list(map(lambda x: (x[1], x[0]), enumerate(nums))))
        score = 0
        for n in nt:
            points, index = n
            if index in marked:
                continue
            marked.update(adj_list[index])
            score += points
        return score
