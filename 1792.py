import heapq


class Solution:
    def get_increase_rate(self, a, b):
        return (a + 1) / (b + 1) - a / b

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        sc = list(
            map(lambda c: (self.get_increase_rate(c[0], c[1]), c[0], c[1]), classes)
        )
        sc = list(map(lambda c: (*c[1], c[0]), enumerate(sc)))
        class_track = {}
        for c in sc:
            class_track[c[-1]] = (c[1], c[2])
        print(sc)
        heapq.heapify(sc)
        while extraStudents:
            c = heapq.heappop(sc)
            _, passed, total, id = c
            print(passed, total)
            if total != class_track[id][1]:
                continue
            heapq.heappush(
                sc,
                (
                    self.get_increase_rate(passed + 1, total + 1),
                    passed + 1,
                    total + 1,
                    id,
                ),
            )
            class_track[id] = (passed + 1, total + 1)
            extraStudents -= 1
        return sum(map(lambda c: c[0] / c[1], class_track.values())) / len(class_track)
