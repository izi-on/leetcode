class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        max_s = 1
        hBars = sorted(hBars)
        vBars = sorted(vBars)
        s_h = {2}
        s_v = {2}
        for i in range(1, len(hBars)):
            space = 1
            if hBars[i] - hBars[i - 1] == 1:
                space += 2
            else:
                space = 2
            s_h.add(space)

        for i in range(1, len(vBars)):
            space = 2
            if vBars[i] - vBars[i - 1] == 1:
                space += 1
            else:
                space = 2
            s_v.add(space)

        max_s = max(s_h & s_v)
        return max_s**2
