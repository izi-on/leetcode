from collections import deque


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        cur = deque(maxlen=3)
        for num in nums:
            if num == cur[-1]:
                continue
            cur.append(num)
            if len(cur) == 3 and (
                (cur[0] < cur[1] > cur[1]) or (cur[0] > cur[1] < cur[2])
            ):
                ans += 1
        return ans
