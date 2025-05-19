from functools import reduce


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if (max(nums)) * 2 >= sum(nums):
            return "none"
        match len(set(nums)):
            case 1:
                return "equilateral"
            case 2:
                return "isosceles"
            case 3:
                return "scalene"
