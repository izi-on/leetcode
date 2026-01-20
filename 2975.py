class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        MOD = 10**9 + 7

        hFences = sorted([1] + hFences + [m])
        h_sides = {
            hFences[j] - hFences[i]
            for i in range(len(hFences))
            for j in range(i + 1, len(hFences))
        }

        vFences = sorted([1] + vFences + [n])
        v_sides = {
            vFences[j] - vFences[i]
            for i in range(len(vFences))
            for j in range(i + 1, len(vFences))
        }

        side = max(h_sides & v_sides, default=0)
        return side**2 % MOD if side else -1
