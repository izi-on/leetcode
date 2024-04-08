from typing import List
from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.points_at_row: dict[int, set[tuple[int, int]]] = defaultdict(set)
        self.count_instance: dict[tuple[int, int], int] = defaultdict(int)

    def add(self, point: List[int]) -> None:
        # print("add", point)
        point_tuple: tuple[int, int] = tuple(point)
        self.points_at_row[point_tuple[0]].add(point_tuple)
        self.count_instance[point_tuple] += 1

    def count(self, point: List[int]) -> int:
        # print("____________________")
        # print("counting for", point)
        point: tuple[int, int] = tuple(point)
        count_valid = 0
        for c_p in self.points_at_row[point[0]] - set([point]):
            i, j = c_p
            to_add_top = (
                self.count_instance[c_p]
                * self.count_instance[((i - abs(point[1] - j)), point[1])]
                * self.count_instance[((i - abs(point[1] - j)), j)]
            )
            # print(
            #     "adding",
            #     to_add_top,
            #     ((i - abs(point[1] - j)), point[1]),
            #     ((i - abs(point[1] - j)), j),
            #     c_p,
            #     point,
            # )
            to_add_bot = (
                self.count_instance[c_p]
                * self.count_instance[((i + abs(point[1] - j)), point[1])]
                * self.count_instance[((i + abs(point[1] - j)), j)]
            )
            # print(
            #     "adding",
            #     to_add_bot,
            #     ((i + abs(point[1] - j)), point[1]),
            #     ((i + abs(point[1] - j)), j),
            #     c_p,
            # )
            count_valid += to_add_top + to_add_bot
        # print("count valid", count_valid)
        # print("____________________")
        return count_valid


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
