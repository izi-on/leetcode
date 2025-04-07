class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        poss_sums = set()
        for num in nums:
            new_poss_sum = set()
            new_poss_sum.add(num)  # by itself
            if num == target:
                return True
            for poss in poss_sums:
                res = poss + num
                new_poss_sum.add(res)
                if target == res:
                    return True
            poss_sums = new_poss_sum.union(poss_sums)
        return False
