from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        track = defaultdict(int)
        for i, n in enumerate(arr):
            track[n] = i
        mem = {}

        def helper(i, j):
            if (i, j) in mem:
                return mem[(i, j)]
            find = arr[j] - arr[i]
            idx = track.get(find, -1)
            if idx == -1 or idx >= i:
                return 0
            mem[(i, j)] = 1 + helper(idx, i)
            return mem[(i, j)]

        return max(
            map(
                lambda x: 0 if x <= 2 else x,
                [
                    2 + helper(i, j)
                    for i in range(len(arr) - 1)
                    for j in range(i + 1, len(arr))
                ],
            )
        )
