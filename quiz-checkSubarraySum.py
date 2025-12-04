class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        track_rems = set([0])
        pref_sum = 0
        for i in range(n - 1):
            ahead_s = pref_sum + nums[i] + nums[i + 1]
            rem = ahead_s % k
            if rem in track_rems:
                return True
            pref_sum += nums[i]
            track_rems.add(pref_sum % k)
        return False
