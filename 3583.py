from collections import defaultdict


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        track_i = defaultdict(int)
        track_j = defaultdict(int)
        ans = 0
        MOD = 10**9 + 7
        for num in nums:
            if not num & 1:
                ans = (ans + track_j[num // 2]) % MOD
            track_j[num] = (track_j[num] + track_i[2 * num]) % MOD
            track_i[num] += 1
        return ans
