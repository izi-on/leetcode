class Solution:
    def numOfWays(self, n: int) -> int:
        x = 6
        y = 6
        MOD = 10**9 + 7
        for _ in range(1, n):
            nx = (3 * x + 2 * y) % MOD
            ny = (2 * x + 2 * y) % MOD
            x, y = nx, ny
        return (x + y) % MOD
