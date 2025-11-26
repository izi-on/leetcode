class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        cur_rem = 0
        for i in range(k):
            cur_rem = (cur_rem * 10 + 1) % k
            if cur_rem == 0:
                return i + 1
        return -1
