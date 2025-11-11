class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # find leftmost
        if n <= 1:
            return n

        nc = n

        # DP
        bit_dp = []
        bit_dp.append(1)
        n = n >> 1
        while n:
            bit_dp.append(2 * bit_dp[-1] + 1)
            n = n >> 1

        def helper(n):
            # print(bin(n)[2:])
            if n == 0:
                return 0
            nc = n
            leftmost = 0
            count = 0
            while nc:
                cbit = nc & 1
                if cbit:
                    leftmost = count
                nc = nc >> 1
                count += 1
            return bit_dp[leftmost] - helper(n ^ (1 << leftmost))

        return helper(nc)
