class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        nums_to_use = []
        for i in range(n, 0, -1):
            nums_to_use.append(i)

        def helper(nums_to_use: list, cur_arrangement, idx):
            while idx < len(cur_arrangement) and cur_arrangement[idx] != 0:
                idx += 1
            if idx == len(cur_arrangement):
                return cur_arrangement
            n_idx = 0
            for n_idx in range(len(nums_to_use)):
                cur = nums_to_use[n_idx]
                if cur != 1 and idx + cur >= len(cur_arrangement):
                    return False
                if cur != 1 and cur_arrangement[cur + idx] != 0:
                    continue

                backtrack = []
                if cur != 1:
                    cur_arrangement[idx] = cur
                    cur_arrangement[idx + cur] = cur
                    backtrack.extend([idx, idx + cur])
                elif cur == 1:
                    cur_arrangement[idx] = cur
                    backtrack.append(idx)

                if helper(
                    nums_to_use[:n_idx] + nums_to_use[n_idx + 1 :],
                    cur_arrangement,
                    idx + 1,
                ):
                    return cur_arrangement
                for b in backtrack:
                    cur_arrangement[b] = 0

            return False

        return helper(nums_to_use, [0 for _ in range(2 * (n - 1) + 1)], 0)
