class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)
        half = (n+m)//2
        l, r = 0, n-1
        while True:
            mid = (l+r)//2
            ptr1 = mid
            ptr2 = half - (ptr1+1) - 1
            left1 = nums1[ptr1] if ptr1 >= 0 else float("-infinity")
            right1 = nums1[ptr1+1] if ptr1 + 1 < n else float("infinity")
            left2 = nums2[ptr2] if ptr2 >= 0 else float("-infinity")
            right2 = nums2[ptr2+1] if ptr2 + 1 < m else float("infinity")
            if (left1 <= right2 and left2 <= right1):
                return min(right1, right2) if (n+m)%2==1 else float(min(right1, right2) + max(left1, left2))/2
            elif left1 > right2:
                r = mid - 1
            elif left2 > right1:
                l = mid + 1

            

