class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        getLongest = {}
        deltas = [[-1,0], [1,0], [0,-1], [0,1]]
        def dfs(i,j):
            # print("visiting: ", (i,j))
            if (i,j) in getLongest:
                # print("cached: ", getLongest[(i,j)])
                return getLongest[(i,j)]
            longest = 0
            for delta in deltas:
                i_n = i + delta[0]
                j_n = j + delta[1]
                if not (0 <= i_n < len(matrix) and 0 <= j_n < len(matrix[0]) and matrix[i][j] < matrix[i_n][j_n]):
                    continue
                longest = max(longest, dfs(i_n, j_n))
            getLongest[(i,j)] = longest + 1
            # print("for ", (i,j), "got longest: ", longest)
            return getLongest[(i,j)]
        longest = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest = max(longest, dfs(i,j))
        return longest
        