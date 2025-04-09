class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return (
            len(list(filter(lambda x: x > k, list(set(nums)))))
            if min(nums) >= k
            else -1
        )
