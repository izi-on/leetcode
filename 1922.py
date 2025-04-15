class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mem = {}
        poss_even = "02468"
        poss_odd = "2357"

        def dp(i, z_poss):
            if i == -1:
                return 1
            if i in mem:
                return mem[i]

            if i % 2 == 0:
                count = 0
                for c in poss_even:
                    if c == "0" and not z_poss:
                        continue
                    count += dp(i - 1, True)
                mem[i] = count
                return count
            else:
                count = 0
                for c in poss_odd:
                    count += dp(i - 1, True)
                mem[i] = count
                return count

        return dp(n - 1, False)
