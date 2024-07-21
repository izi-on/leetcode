from collections import defaultdict


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:

        matrix = [[0] * k for _ in range(k)]

        def toposort(adj_list: dict[int, set], rev_adj_list: dict[int, set]):
            queue = []
            for i in range(1, k + 1):
                val = rev_adj_list[i]
                if len(val) == 0:
                    queue.append(i)
            answer = []
            while len(queue) > 0:
                n = len(queue)
                for _ in range(n):
                    cur_node = queue.pop()
                    answer.append(cur_node)
                    for child in adj_list[cur_node]:
                        rev_adj_list[child].remove(cur_node)
                        if len(rev_adj_list[child]) == 0:
                            queue.append(child)
            return answer

        adj_list_row = defaultdict(set)
        rev_adj_list_row = defaultdict(set)
        for cond in rowConditions:
            adj_list_row[cond[0]].add(cond[1])
            rev_adj_list_row[cond[1]].add(cond[0])

        r_order = toposort(adj_list_row, rev_adj_list_row)
        if len(r_order) != k:
            return []

        adj_list_col = defaultdict(set)
        rev_adj_list_col = defaultdict(set)
        for cond in colConditions:
            adj_list_col[cond[0]].add(cond[1])
            rev_adj_list_col[cond[1]].add(cond[0])

        c_order = toposort(adj_list_col, rev_adj_list_col)
        if len(c_order) != k:
            return []
        c_num_to_idx = {c_order[i]: i for i in range(k)}

        for i in range(k):
            matrix[i][c_num_to_idx[r_order[i]]] = r_order[i]
        return matrix
