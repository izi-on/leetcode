class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        n = numCourses
        pre_reqs = [set() for _ in range(n)]
        processed = set()
        adj_list = [set() for _ in range(n)]
        for edge in prerequisites:
            u, v = edge
            adj_list[v].add(u)

        def set_prereqs(course: int):
            if course in processed:
                return pre_reqs[course]
            processed.add(course)
            cur_pr = set([course])
            for neighbour in adj_list[course]:
                cur_pr.update(set_prereqs(neighbour))
            pre_reqs[course] = cur_pr
            return cur_pr

        for i in range(n):
            set_prereqs(i)

        print(pre_reqs)
        # queries
        ans = []
        for query in queries:
            u, v = query
            ans.append(u in pre_reqs[v])
        return ans
