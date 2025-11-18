class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        next_stream = 1
        for t in target:
            ans += ["Push"] * (t - next_stream) + ["Pop"] * (t - next_stream)
            ans += ["Push"]
            next_stream = t + 1
        return ans
