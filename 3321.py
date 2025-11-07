from collections import defaultdict
import heapq


class Heap:
    def __init__(self, max_s=float("inf")):
        self.max_heap = []
        self.min_heap = []
        self.max_size = max_s
        self.count = defaultdict(int)

    def increment(self, val):
        self.count[val] += 1
        heapq.heappush(self.max_heap, (-self.count[val], -val))
        heapq.heappush(self.min_heap, (self.count[val], val))
        self.clean_heap()

    def decrement(self, val):
        self.count[val] -= 1
        heapq.heappush(self.max_heap, (-self.count[val], -val))
        heapq.heappush(self.min_heap, (self.count[val], val))
        if self.count[val] == 0:
            del self.count[val]
        self.clean_heap()

    def pop_min(self):
        freq, val = heapq.heappop(self.min_heap)
        del self.count[val]
        self.clean_heap()
        return freq, val

    def pop_max(self):
        freq, val = heapq.heappop(self.max_heap)
        freq, val = -freq, -val
        del self.count[val]
        self.clean_heap()
        return freq, val

    def push_freq_val(self, freq, val):
        assert val not in self.count
        heapq.heappush(self.min_heap, (freq, val))
        heapq.heappush(self.max_heap, (-freq, -val))
        self.count[val] = freq
        self.clean_heap()

    def get_min(self):
        if not self.min_heap:
            return None
        return self.min_heap[0]

    def get_max(self):
        if not self.max_heap:
            return None
        freq, val = self.max_heap[0]
        return (-freq, -val)

    def evict_if_full(self):
        if self.max_size and len(self) > self.max_size:
            freq, val = heapq.heappop(self.min_heap)
            del self.count[val]
            self.clean_heap()
            return (freq, val)

    def clean_heap(self):
        while (
            self.max_heap
            and self.count.get(-self.max_heap[0][1]) != -self.max_heap[0][0]
        ):
            heapq.heappop(self.max_heap)
        while (
            self.min_heap and self.count.get(self.min_heap[0][1]) != self.min_heap[0][0]
        ):
            heapq.heappop(self.min_heap)

    def __sizeof__(self) -> int:
        return len(self.count.keys())

    def __len__(self):
        return len(self.count.keys())

    def is_full(self):
        return len(self) >= self.max_size

    def has_val(self, val):
        return val in self.count.keys()


class Helper:
    def __init__(self, x=float("inf")):
        self.top_x = Heap(x)
        self.rest = Heap()
        self.cur_sum = 0

    def add(self, val):
        if self.top_x.has_val(val):
            self.top_x.increment(val)
            self.cur_sum += val
        else:
            self.rest.increment(val)
        self.exchange()

    def remove(self, val):
        if self.top_x.has_val(val):
            self.top_x.decrement(val)
            self.cur_sum -= val
        else:
            self.rest.decrement(val)
        self.exchange()

    def exchange(self):
        while not self.top_x.is_full():
            if self.rest.get_max() is None:
                break
            freq, val = self.rest.pop_max()
            self.top_x.push_freq_val(freq, val)
            self.cur_sum += val * freq
        while (
            self.top_x.get_min()
            and self.rest.get_max()
            and self.top_x.get_min() < self.rest.get_max()
        ):
            txfreq, txval = self.top_x.pop_min()
            rfreq, rval = self.rest.pop_max()
            self.top_x.push_freq_val(rfreq, rval)
            self.rest.push_freq_val(txfreq, txval)
            self.cur_sum += (rfreq * rval) - (txfreq * txval)

    def get_sum(self):
        return self.cur_sum


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        h = Helper(x)
        ans = []
        for i in range(k):
            num = nums[i]
            h.add(num)
        ans.append(h.get_sum())
        for i in range(1, len(nums) - k + 1):
            to_add = nums[i + k - 1]
            to_remove = nums[i - 1]
            h.remove(to_remove)
            h.add(to_add)
            ans.append(h.get_sum())
        return ans
