class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # sub_rem  = rem_s
        # pref_rem - max_sub_rem = rem_s
        # (pref_rem % p - max_sub_rem % p) % p = rem_s % p
        # (pref_rem % p - rem_s % p) % p = max_sub_rem % p
        s = sum(nums)
        rem_s = s % p
        if rem_s == 0:
            return 0
        map_max_rem_idx = {}
        map_max_rem_idx[0] = -1
        psum = 0
        tmin = len(nums)
        for i in range(len(nums)):
            psum += nums[i]
            prem = psum % p
            target = (prem - rem_s) % p
            if target in map_max_rem_idx:
                tmin = min(tmin, i - map_max_rem_idx[target])
            map_max_rem_idx[prem] = i
        return tmin if tmin != len(nums) else -1
