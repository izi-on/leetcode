from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        done = set()
        sinks = set()
        for i in range(numCourses):
            sinks.add(i)
        for prereq in prerequisites:
            adj_list[prereq[0]].append(prereq[1])
            try:
                sinks.remove(prereq[1])
            except:
                pass

        impossible = False

        def dfs(cur, visited):
            nonlocal adj_list
            nonlocal impossible
            if cur in visited:
                impossible = True
                return []
            if cur in done:
                return []
            visited.add(cur)
            ans = []
            for prereq in adj_list[cur]:
                ans += dfs(prereq, visited)
                if impossible:
                    return []
            visited.remove(cur)
            ans += [cur]
            done.add(cur)
            return ans

        ans = []
        for sink in sinks:
            ans += dfs(sink, set())
            if impossible:
                return []
        return ans
