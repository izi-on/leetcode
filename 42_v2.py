class Solution:
    def trap(self, height: List[int]) -> int:
        ptr1, ptr2 = 0, len(height) - 1
        max_left = 0
        max_right = 0

        ans = 0
        while ptr1 <= ptr2:
            max_left = max(max_left, height[ptr1])
            max_right = max(max_right, height[ptr2])

            if max_left <= max_right:
                ans += max_left - height[ptr1]
                ptr1 += 1

            if max_right <= max_left and ptr1 <= ptr2:
                ans += max_right - height[ptr2]
                ptr2 -= 1

        return ans
