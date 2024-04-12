class Solution:
    def trap(self, height: List[int]) -> int:
        # get max from the left
        highest_to_left = [-1] * len(height)
        track_max = 0
        for i in range(len(height)):
            highest_to_left[i] = track_max
            track_max = max(track_max, height[i])

        # get max from the left
        highest_to_right = [-1] * len(height)
        track_max = 0
        for i in range(len(height) - 1, -1, -1):
            highest_to_right[i] = track_max
            track_max = max(track_max, height[i])

        # calculate water
        water = 0
        for i in range(len(height)):
            smallest_height = min(highest_to_right[i], highest_to_left[i])
            to_add = max(0, smallest_height - height[i])
            water += to_add
        return water
