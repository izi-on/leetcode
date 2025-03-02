class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        ptr1, ptr2 = 0, 0
        ans = []
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            id1, val1 = nums1[ptr1]
            id2, val2 = nums2[ptr2]
            if id1 == id2:
                ans.append((id1, val1 + val2))
                ptr1 += 1
                ptr2 += 1
            elif id1 < id2:
                ans.append((id1, val1))
                ptr1 += 1
            else:
                ans.append((id2, val2))
                ptr2 += 1
        ans.extend(nums1[ptr1:])
        ans.extend(nums1[ptr2:])
        return ans
