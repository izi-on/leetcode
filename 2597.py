from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = 0

        def helper(cur, idx, forbidden):
            nonlocal count
            if idx == len(nums):
                count += 1
                return
            if nums[idx] not in forbidden:
                cur.append(nums[idx])
                forbidden[nums[idx] + k] += 1
                forbidden[nums[idx] - k] += 1
                helper(cur, idx + 1, forbidden)
                cur.pop()
                forbidden[nums[idx] + k] -= 1
                if forbidden[nums[idx] + k] == 0:
                    del forbidden[nums[idx] + k]
                forbidden[nums[idx] - k] -= 1
                if forbidden[nums[idx] - k] == 0:
                    del forbidden[nums[idx] - k]
            helper(cur, idx + 1, forbidden)

        helper([], 0, defaultdict(int))
        return count
