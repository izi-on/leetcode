class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monostack = []  # (height, start)
        ans = 0
        for i, h in enumerate(heights):
            ps = i
            while monostack and monostack[-1][0] >= h:
                ph, ps = monostack.pop()
                width = i - ps
                height = ph
                ans = max(ans, width * height)
            monostack.append((h, ps))
        i = len(heights)
        while monostack:
            ph, ps = monostack.pop()
            width = i - ps
            height = ph
            ans = max(ans, width * height)
        return ans
