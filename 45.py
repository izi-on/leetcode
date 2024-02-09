from collections import deque


class Solution:
    def jump(self, nums: List[int]) -> int:
        bfs = deque()
        bfs.append((nums[0], 0))
        steps = 0
        track_unexplored = 0
        while bfs:
            n = len(bfs)
            for _ in range(n):
                num, i = bfs.popleft()
                if i == len(nums) - 1:
                    return steps
                for j in range(track_unexplored, min(i + num + 1, len(nums))):
                    bfs.append((nums[j], j))
                    track_unexplored = j
                track_unexplored += 1
            steps += 1
        return -1
