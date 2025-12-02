class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries = sorted(batteries)
        live = batteries[-n:]
        extra = sum(batteries[:-n])

        for i in range(n - 1):
            if extra < (live[i + 1] - live[i]) * (i + 1):
                return live[i] + extra // (i + 1)
            extra -= (live[i + 1] - live[i]) * (i + 1)
        return live[n - 1] + extra // n
