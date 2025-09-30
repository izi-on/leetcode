from functools import reduce


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        mem = {}

        def helper(i, j):
            if j - i < 2:
                return 0
            if (i, j) in mem:
                return mem[(i, j)]
            min_sum = float("inf")
            for k in range(i + 1, j):
                # we add an edge from i to k
                cur_sum = values[i] * values[j] * values[k]
                sum_triangles_left = helper(i, k)
                sum_triangles_right = helper(k, j)
                min_sum = min(
                    min_sum, cur_sum + sum_triangles_left + sum_triangles_right
                )
            mem[(i, j)] = min_sum
            return min_sum

        return helper(0, len(values) - 1)
