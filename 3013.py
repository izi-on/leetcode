from collections import defaultdict
import heapq


class MinTracker:
    def __init__(self, k):
        self.k = k
        self.track_cand = defaultdict(int)
        self.track_k = defaultdict(int)
        self.heap_k = []
        self.heap_cand = []
        self.sum = 0
        self.count_k = 0

    def peak(self, heap, track):
        while heap and track[heap[0]] == 0:
            heapq.heappop(heap)
        return heap[0] if heap else None

    def pop(self, heap, track):
        while heap and track[heap[0]] == 0:
            heapq.heappop(heap)
        track[heap[0]] -= 1
        return heapq.heappop(heap)

    def push(self, val, heap, track):
        heapq.heappush(heap, val)
        track[val] += 1

    def submit(self, val):
        self.push(val, self.heap_cand, self.track_cand)
        self.exchange()

    def remove(self, val):
        # print("removing", val, "current: ", self.track_k[-val], self.track_cand[val])
        if self.track_cand[val] > 0:
            self.track_cand[val] -= 1
        elif self.track_k[-val] > 0:
            self.track_k[-val] -= 1
            self.sum -= val
            self.count_k -= 1
        self.exchange()

    def exchange(self):
        while self.count_k < self.k and self.peak(self.heap_cand, self.track_cand):
            val = self.pop(self.heap_cand, self.track_cand)
            self.push(-val, self.heap_k, self.track_k)
            self.count_k += 1
            self.track_k[val] += 1
            self.sum += val

        while (
            self.peak(self.heap_cand, self.track_cand) is not None
            and self.peak(self.heap_k, self.track_k) is not None
            and self.peak(self.heap_cand, self.track_cand)
            < -self.peak(self.heap_k, self.track_k)
        ):
            val_k = -self.pop(self.heap_k, self.track_k)
            val_cand = self.pop(self.heap_cand, self.track_cand)
            self.push(-val_cand, self.heap_k, self.track_k)
            self.push(val_k, self.heap_cand, self.track_cand)
            self.sum = self.sum - val_k + val_cand

    def get_sum(self):
        return self.sum


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        s_ptr = 1
        s = nums[0] + nums[s_ptr]
        tracker = MinTracker(k - 2)
        for i in range(2, min(len(nums), s_ptr + dist + 1)):
            tracker.submit(nums[i])

        s += tracker.get_sum()
        t_min = s

        for _ in range(2, len(nums) - k + 2):  # possible second
            s -= nums[s_ptr] + tracker.get_sum()
            s_ptr += 1
            print("before remove", tracker.get_sum())
            tracker.remove(nums[s_ptr])
            print("after remove:", tracker.get_sum())
            s += nums[s_ptr]
            if s_ptr + dist < len(nums):
                tracker.submit(nums[s_ptr + dist])
            s += tracker.get_sum()
            t_min = min(t_min, s)
            print(
                "s_ptr:",
                s_ptr,
                "tmin",
                t_min,
                "max dist",
                s_ptr + dist,
                "tracker sum",
                tracker.get_sum(),
            )

        return t_min
