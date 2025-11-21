import math


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        return int(-1 / 2 + math.sqrt(1 / 4 + 2 * n))
