class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        mem = {}

        def helper(idx1, idx2, state):
            nonlocal mem
            if idx1 == len(nums1) or idx2 == len(nums2):
                return 0 if state == 1 else -float("inf")
            if (idx1, idx2, state) in mem:
                return mem[(idx1, idx2, state)]

            ans = -float("inf")
            ans = nums1[idx1] * nums2[idx2] + helper(idx1 + 1, idx2 + 1, 1)
            ans = max(ans, helper(idx1 + 1, idx2, state))
            ans = max(ans, helper(idx1, idx2 + 1, state))
            mem[(idx1, idx2, state)] = ans
            return ans

        ans = helper(0, 0, 0)
        print(ans)
        return ans
