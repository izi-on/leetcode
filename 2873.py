class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # what is the vim macro to replace these sqrt brackets with paranthesis instead
        left_max = []
        right_max = []
        for i in range(len(nums)):
            left_max.append(max(nums[i], left_max[-1] if left_max else -1))
            right_max.insert(0, max(nums[-i - 1], right_max[0] if right_max else -1))
        ans = 0
        for i in range(1, len(nums) - 1):
            ans = max(ans, (left_max[i - 1] - nums[i]) * right_max[i + 1])
        return ans
