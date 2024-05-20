from collections import defaultdict, deque


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        memoized = {}

        def helper(idx, isEven):
            nonlocal memoized
            if idx == len(nums):
                return 0 if isEven else -float("infinity")
            if (idx, isEven) in memoized:
                return memoized[(idx, isEven)]
            no_flip = helper(idx + 1, isEven) + nums[idx]
            flip = helper(idx + 1, not isEven) + (nums[idx] ^ k)
            memoized[(idx, isEven)] = max(flip, no_flip)
            return memoized[(idx, isEven)]

        helper(0, True)
        return memoized[(0, True)]
