from collections import defaultdict
import string


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        dist = [[float("inf") for _ in range(26)] for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for u, v, w in zip(original, changed, cost):
            dist[ord(u) - ord("a")][ord(v) - ord("a")] = min(
                dist[ord(u) - ord("a")][ord(v) - ord("a")], w
            )

        for k in range(26):
            for i in range(26):
                if dist[i][k] == float("inf"):
                    continue
                for j in range(26):
                    nk = dist[i][k] + dist[k][j]
                    dist[i][j] = min(dist[i][j], nk)

        ans = sum(
            list(
                [
                    dist[ord(u) - ord("a")][ord(v) - ord("a")]
                    for u, v in zip(source, target)
                ]
            )
        )
        return ans if ans != float("inf") else -1
