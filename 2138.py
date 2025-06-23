class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ns = list(s)
        ns.extend([fill] * (((len(ns) + k - 1) // k) * k - len(ns)))
        return ["".join(ns[i : i + k]) for i in range(0, len(ns), k)]
