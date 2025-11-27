class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        for i in range(len(gain)):
            gain[i] = gain[i - 1] + gain[i] if i > 0 else gain[i]
        return max(*gain, 0)
