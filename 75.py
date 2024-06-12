class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        cursor = 0
        while l <= cursor <= r:
            if nums[cursor] == 0:
                nums[l], nums[cursor] = nums[cursor], nums[l]
                if l == cursor:
                    cursor += 1
                l += 1
            elif nums[cursor] == 2:
                nums[r], nums[cursor] = nums[cursor], nums[r]
                if r == cursor:
                    cursor += 1
                r -= 1
            else:
                cursor += 1
