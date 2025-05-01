class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(
            list(filter(lambda x: x % 2 == 0, list(map(lambda x: len(str(x)), nums))))
        )
