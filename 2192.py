from collections import defaultdict, deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = {}
        rev_adj_list = {}
        removed_count = defaultdict(int)
        for i in range(n):
            adj_list[i] = []
            rev_adj_list[i] = []
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            rev_adj_list[edge[1]].append(edge[0])

        # print(rev_adj_list)

        cur = deque()
        for node, nbs in rev_adj_list.items():
            if len(nbs) == 0:
                cur.append(node)

        answer: list[set[int]] = [set() for i in range(n)]
        while len(cur) > 0:
            i = cur.popleft()
            for parent in rev_adj_list[i]:
                answer[i].add(parent)
                answer[i] = answer[i].union(answer[parent])
            for child in adj_list[i]:
                removed_count[child] += 1
                # print("_______________")
                # print(removed_count[child])
                # print(rev_adj_list[child])
                if removed_count[child] == len(rev_adj_list[child]):
                    cur.append(child)

        answer = list(map(lambda x: sorted(list(x)), answer))
        return answer
