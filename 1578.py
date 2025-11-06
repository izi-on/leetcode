class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        groups = []
        cur_group = [0]
        prev = None
        for i, c in enumerate(colors):
            if c != prev:
                groups.append(cur_group)
                cur_group = []
            cur_group.append(neededTime[i])
            prev = c
        groups.append(cur_group)

        ans = 0
        # print(groups)
        for g in groups:
            ans += sum(g) - max(g)
        return ans
