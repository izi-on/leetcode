class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        n = len(spells)
        m = len(potions)

        potions = sorted(potions)

        ans = []
        for i in range(n):
            spell = spells[i]
            target = success / spell
            l, r = 0, m - 1
            p_ans = m
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                    p_ans = mid
            ans.append(m - p_ans)
        return ans
