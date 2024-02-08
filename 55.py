class Solution:
    def canJump(self, nums: List[int]) -> bool:
        trackJumpPos = set()
        for i, num in enumerate(nums[:-1]):
            trackJumpPos.add(i + num)
            if i in trackJumpPos:
                trackJumpPos.remove(i)
            if not trackJumpPos:
                return False
        return True
