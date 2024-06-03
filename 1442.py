from collections import defaultdict


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count_0 = 0
        for i in range(len(arr)):
            cur_xor = 0
            for j in range(i, len(arr)):
                cur_xor ^= arr[j]
                if cur_xor == 0:
                    count_0 += j - i
        return count_0
