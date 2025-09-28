class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        triplets = [(nums[i - 2], nums[i - 1], nums[i]) for i in range(2, len(nums))]

        def is_valid(triplet):
            fs, snd, trd = triplet
            return fs < snd + trd

        for triplet in triplets:
            if is_valid(triplet):
                return sum(triplet)
        return 0
