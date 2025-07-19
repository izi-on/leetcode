class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        maxh = []
        minh = []
        sum_l = 0
        left = [-1 for _ in range(n * 3)]
        for i in range(n):
            heapq.heappush(maxh, -nums[i])
            sum_l += nums[i]
            left[i] = sum_l
        for i in range(n, 2 * n):
            heapq.heappush(maxh, -nums[i])
            sum_l += nums[i]
            popped = heapq.heappop(maxh)
            sum_l += popped  # negative
            left[i] = sum_l

        minh = []
        sum_r = 0
        for i in range(2 * n, 3 * n):
            heapq.heappush(minh, nums[i])
            sum_r += nums[i]

        ans = float("inf")
        for i in range(2 * n, n - 1, -1):
            c = left[i - 1] - sum_r
            # print(c, sum_r)
            ans = min(c, ans)
            heapq.heappush(minh, nums[i - 1])
            popped = heapq.heappop(minh)
            sum_r -= popped
            sum_r += nums[i - 1]

        # print(left)

        return ans
