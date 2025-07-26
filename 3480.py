from collections import defaultdict


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = defaultdict(list)
        for pair in conflictingPairs:
            if pair[0] > pair[1]:
                pair[0], pair[1] = pair[1], pair[0]
            right[pair[1]].append(pair[0])

        ans = 0
        left = [0, 0]
        bonus = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            new_left = right[i]

            for elem in new_left:
                if elem > left[0]:
                    left.insert(0, elem)
                    left.pop()
                elif elem > left[1]:
                    left.insert(1, elem)
                    left.pop()

            ans += i - left[0]
            bonus[left[0]] += left[0] - left[1]
        return ans + max(bonus)
