class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num & 1 == 0:
                ans.append(-1)
            else:
                bit = 1
                while bit & num:
                    bit <<= 1
                bit >>= 1
                ans.append(num - bit)
        return ans
