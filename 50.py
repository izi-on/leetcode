class Solution:
    def myPow(self, x: float, n: int) -> float:
        dp = {}
        def helper():
            nonlocal dp
            if n == 0: 
                return 1
            if n == 1:
                return x
            if n < 0:
                return 1/self.myPow(x, -n)
            if n in dp:
                return dp[n]
            half = self.myPow(x, n // 2) 
            try: 
                if n % 2 == 0:
                    res = half*half
                else:
                    res = x*half*half
            finally:
                dp[n] = res
                return res 
        return helper()