class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        count_unoccupied = m * n - len(guards) - len(walls)
        seen = set()
        deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        walls = set([(x[0], x[1]) for x in walls])
        guards = set([(x[0], x[1]) for x in guards])

        def mark_seen(i, j):
            nonlocal count_unoccupied
            for delta in deltas:
                cur = [i, j]
                # print("moving:", cur, delta)
                while 0 <= cur[0] + delta[0] < m and 0 <= cur[1] + delta[1] < n:
                    # print(cur[0], cur[1])
                    cur[0] += delta[0]
                    cur[1] += delta[1]
                    if (cur[0], cur[1]) in walls or (cur[0], cur[1]) in guards:
                        # print("wall, no count")
                        break
                    if (cur[0], cur[1]) in seen:
                        # print("seen, no count")
                        continue
                    seen.add((cur[0], cur[1]))
                    count_unoccupied -= 1

        for g in guards:
            i, j = g
            mark_seen(i, j)
        return count_unoccupied
