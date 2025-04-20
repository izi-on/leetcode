from collections import defaultdict
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq_count = defaultdict(int)
        for ans in answers:
            freq_count[ans] += 1

        rabbit_count = 0
        for x_of_same_color, amt_answered_x in freq_count.items():
            # at best, all who answered intersect with the same color
            rabbit_count += (x_of_same_color + 1) * (
                (amt_answered_x + x_of_same_color) // (x_of_same_color + 1)
            )
        return rabbit_count
