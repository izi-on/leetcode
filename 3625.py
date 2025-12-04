from collections import defaultdict


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            a, b = max(a, b), min(a, b)
            if b == 0:
                return a
            return gcd(b, a % b)

        n = len(points)
        map_slope_count = defaultdict(int)
        map_slope_start_count = defaultdict(lambda: defaultdict(int))
        map_slope_start_count_length = defaultdict(
            lambda: defaultdict(lambda: defaultdict(int))
        )
        map_slope_length = defaultdict(lambda: defaultdict(int))
        count = 0
        count_equal_length = 0
        for i in range(n):
            for j in range(i + 1, n):
                p1 = tuple(points[i])
                p2 = tuple(points[j])
                p1, p2 = max(p1, p2), min(p1, p2)
                slope_num = p2[1] - p1[1]
                slope_den = p2[0] - p1[0]
                if slope_den == 0:
                    start = p1[0]
                    length = abs(p2[1] - p1[1])
                    slope = None
                else:
                    _gcd = gcd(abs(slope_num), abs(slope_den))
                    slope_den //= _gcd
                    slope_num //= _gcd
                    start = slope_den * p1[1] - slope_num * p1[0]
                    slope = (slope_num, slope_den)
                    length = (p1[1] - p2[1]) ** 2 + (p1[0] - p2[0]) ** 2

                count += map_slope_count[slope] - map_slope_start_count[slope][start]
                count_equal_length += (
                    map_slope_length[slope][length]
                    - map_slope_start_count_length[slope][start][length]
                )

                map_slope_count[slope] += 1
                map_slope_start_count[slope][start] += 1
                map_slope_length[slope][length] += 1
                map_slope_start_count_length[slope][start][length] += 1
                print("count", count)
        return count - count_equal_length // 2
