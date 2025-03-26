class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums: list[int] = [num for row in grid for num in row]
        m_n = min(nums)
        if any(map(lambda num: (num - m_n) % x, nums)):
            return -1
        nums = sorted(nums)
        median = nums[len(nums) // 2]
        return sum(map(lambda num: abs(median - num) // x, nums))
