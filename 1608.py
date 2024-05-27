class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)
        largest_satisfies = -1
        for i in range(1, len(nums) + 1):
            if i > nums[-i]:
                if largest_satisfies == nums[-i]:
                    return -1
                break
            largest_satisfies = i
        return largest_satisfies
