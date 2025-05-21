from collections import defaultdict


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        p_q_l = defaultdict(int)
        p_q_r = defaultdict(int)
        for query in queries:
            p_q_l[query[0]] += 1
            p_q_r[query[1]] += 1
        cur_overlap = 0
        for i in range(n):
            cur_overlap += p_q_l[i]
            if nums[i] > cur_overlap:
                return False
            cur_overlap -= p_q_r[i]
        return True
