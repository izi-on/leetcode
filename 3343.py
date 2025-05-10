from collections import defaultdict


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        possible_sums = defaultdict(lambda: defaultdict(int))
        n_ = len(num)
        for c in num:
            n = int(c)
            possible_sums[1][n] += 1
            new_poss_sums = possible_sums.copy()
            for with_x_nums, amt_permutations_dict in possible_sums.items():
                for sum_t, amt_permutations in amt_permutations_dict.items():
                    new_poss_sums[with_x_nums + 1][sum_t + n] += amt_permutations
            possible_sums = new_poss_sums

        if n_ % 2 == 0:
            # one group
            possible_sums[n // 2]
