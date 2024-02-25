from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def helper(cur, adj_list, visited, finished):
            if cur in visited:
                return True
            if cur in finished:
                return False
            visited.add(cur)
            for nxt in adj_list[cur]:
                if helper(nxt, adj_list, visited, finished):
                    return True
            visited.remove(cur)
            finished.add(cur)
            return False

        # build tree
        adj_list = defaultdict(list[int])
        for prereq in prerequisites:
            adj_list[prereq[0]].append(prereq[1])

        # go through tree and check for any cycles
        finished = set()
        for i in range(numCourses):
            if helper(i, adj_list, set(), finished):
                return False
        return True
