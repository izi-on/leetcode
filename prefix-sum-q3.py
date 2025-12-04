class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        psum_e = [0] * (n + 2)
        psum_o = [0] * (n + 2)
        for i in range(n):
            num = nums[i]
            if i % 2:
                psum_o[i + 1] += num
            else:
                psum_e[i + 1] += num
            psum_o[i + 1] += psum_o[i]
            psum_e[i + 1] += psum_e[i]
        psum_o[n + 1] = psum_o[n]
        psum_e[n + 1] = psum_e[n]

        ways = 0
        for i in range(n):
            # attempt to rem i
            p_idx = i + 1
            p_e = psum_e[p_idx - 1] + psum_o[n + 1] - psum_o[p_idx]
            p_o = psum_o[p_idx - 1] + psum_e[n + 1] - psum_e[p_idx]
            if p_e == p_o:
                ways += 1
        return ways
