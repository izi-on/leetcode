import heapq


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # init the window
        track_max = []
        heapq.heapify(track_max)

        visited = set()

        # init heap
        for i in range(len(nums[: k - 1])):
            heapq.heappush(track_max, (-1 * nums[i], i))

        answer = []
        for i in range(len(nums) - k + 1):
            # print("Looking at ", i, i + k - 1)
            if i != 0:
                visited.add((-1 * nums[i - 1], i - 1))
            heapq.heappush(track_max, (-1 * nums[i + k - 1], i + k - 1))

            cur_max = heapq.heappop(track_max)
            while cur_max in visited:
                cur_max = heapq.heappop(track_max)
            heapq.heappush(track_max, cur_max)
            answer.append(-1 * cur_max[0])

        return answer
