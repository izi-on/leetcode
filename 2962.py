class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_elem = max(nums)
        count_max_elem = 0
        head = 0

        def count(cur):
            nonlocal count_max_elem
            if cur == max_elem:
                count_max_elem += 1

        def rm(cur):
            nonlocal count_max_elem
            if cur == max_elem:
                count_max_elem -= 1

        ans = 0
        for i in range(n):
            while head < n and count_max_elem < k:
                count(nums[head])
                head += 1
            if count_max_elem >= k:
                ans += n - head + 1
            # print(i, head, count_max_elem)
            rm(nums[i])
        return ans
