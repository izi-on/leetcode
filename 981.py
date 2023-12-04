from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.data: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        bin_search = self.data[key]
        left, right = 0, len(bin_search)-1
        f_time, f_val = -1, ""
        while left <= right:
            mid = (left + right) // 2
            time, val = bin_search[mid]
            if time <= timestamp:
                f_time, f_val = time, val
                left = mid + 1
            else:
                right = mid - 1
        return f_val



