class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # we notice that in the worst case scenario answer is n+1
        n = len(nums)
        i = 0
        while i < n:
            num = nums[i]
            if num - 1 == i:
                i += 1
                continue
            if 0 < num <= n:
                if nums[i] == nums[num - 1]:
                    i += 1
                    continue
                nums[i], nums[num - 1] = nums[num - 1], num
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
