class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        st_min = [None] * 4 * n

        def update(v, sl, sr, k, val):
            if sl == sr and sl == k:
                st_min[k] = val
            else:
                mid = (sl + sr) // 2
                if k <= mid:
                    update(2 * v, sl, mid, k, val)
                else:
                    update(2 * v + 1, mid + 1, sr, k, val)
                st_min[v] = min(st_min[2 * v], st_min[2 * v + 1])

        def search(v, sl, sr, l, r):
            if l > r:
                return float("inf"), []
            if l == sl and r == sr:
                return st_min[v], [sl]
            else:
                mid = (sl + sr) // 2
                lidxs = []
                ridxs = []
                cur_min = st_min[v]
                _, lidxs = search(2 * v, sl, mid, l, min(mid, r))
                _, ridxs = search(2 * v + 1, mid, sr, max(mid + 1, l), r)
                return cur_min, lidxs + ridxs

        for i, t in enumerate(target):
            update(1, 0, n - 1, i, t)

        def helper(l, r, cur_height):
            if l > r:
                return 0
            if l == r:
                return search(1, 0, n - 1, l, l)[0] - cur_height
            cur_min, idxs = search(1, 0, n - 1, l, r)
            idxs += [r]
            ans = cur_min - cur_height
            cur_idx = 0
            for idx in idxs:
                ans += helper(cur_idx, idx - 1, cur_min)
                cur_idx = idx + 1
            return ans

        return helper(0, n - 1, 0)
