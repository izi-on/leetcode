class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z_1, z_2 = (
            any(list(map(lambda x: x == 0, nums1))),
            any(list(map(lambda x: x == 0, nums2))),
        )
        min_1, min_2 = (
            sum(list(map(lambda x: x if x != 0 else 1, nums1))),
            sum(list(map(lambda x: x if x != 0 else 1, nums2))),
        )

        if z_1 and z_2:
            return max(min_1, min_2)
        elif z_1 and not z_2:
            return min_2 if min_1 <= min_2 else -1
        elif z_2 and not z_1:
            return min_1 if min_2 <= min_1 else -1
        elif not z_1 and not z_2:
            return min_1 if min_1 == min_2 else -1
