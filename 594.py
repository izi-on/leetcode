class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_track = [-float("inf")]
        for n in nums:
            max_track.append(max(max_track[-1], n))
        max_track = max_track[1:]

        i = 1
        tail_idx = 0
        while i < len(max_track):


