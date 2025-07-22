class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        head = -1
        cur = 0
        num_to_idx = {}
        ans = -float("inf")
        for i in range(len(nums)):
            cur += nums[i]
            if nums[i] in num_to_idx:
                remove_until = num_to_idx[nums[i]]
                while head < remove_until:
                    head += 1
                    del num_to_idx[nums[head]]
                    cur -= nums[head]
            num_to_idx[nums[i]] = i
            ans = max(ans, cur)
        return ans
