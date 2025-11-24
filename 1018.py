class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur = 0
        ans = []
        for n in nums:
            cur = (cur << 1) | n
            ans.append(not (cur % 5))
        return ans
