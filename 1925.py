import math


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    return gcd(b, a % b)


class Solution:
    def countTriples(self, n: int) -> int:
        limit = int(math.sqrt(n))
        res = 0
        for u in range(2, limit + 1):
            for v in range(1, u + 1):
                a = u**2 - v**2
                b = 2 * u * v
                if gcd(a, b) != 1 or (a - b) % 2 == 0:
                    continue
                c = u**2 + v**2
                if c > n:
                    continue
                res += 2 * (n // c)
        return res
