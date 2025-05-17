from collections import defaultdict


class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        def is_diff_one(word1, word2):
            n_1, n_2 = len(word1), len(word2)
            if n_1 != n_2:
                return False
            count_diff = 0
            for i in range(n_2):
                if word1[i] != word2[i]:
                    count_diff += 1
                    if count_diff == 2:
                        return False
            return True

        n = len(words)
        graph: dict[int, list[int]] = defaultdict(list)
        rev_graph: dict[int, list[int]] = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if groups[i] != groups[j] and is_diff_one(words[i], words[j]):
                    graph[i].append(j)

        # find longest path in graph
        dp = {}

        def helper(cur):
            if cur in dp:
                return dp[cur][0], cur
            max_path = 0
            max_prev = -1
            for nn in graph[cur]:
                max_sp, prev = helper(nn)
                if max_sp > max_path:
                    max_path = max_sp
                    max_prev = prev
            dp[cur] = (max_path + 1, max_prev)
            return max_path + 1, cur

        for i in range(n):
            helper(i)

        # find index of biggest subsequence
        max_ss = -1
        max_num = -1
        for k, v in dp.items():
            if v[0] > max_ss:
                max_ss = v[0]
                max_num = k

        ans = [max_num]
        cur_max_prev = dp[max_num][1]
        while cur_max_prev != -1:
            ans.append(cur_max_prev)
            cur_max_prev = dp[cur_max_prev][1]

        return list(map(lambda i: words[i], ans))
