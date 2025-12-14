class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def helper(s, e, k):
            if s == e:
                return nums[s]
            pivot = nums[s]
            lt_ptr, i, gt_ptr = s + 1, s + 1, e
            while i <= gt_ptr:
                if nums[i] < pivot:
                    nums[lt_ptr], nums[i] = nums[i], nums[lt_ptr]
                    lt_ptr += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt_ptr] = nums[gt_ptr], nums[i]
                    gt_ptr -= 1
                else:
                    i += 1

            amt_larger = e - gt_ptr
            amt_smaller = lt_ptr - s - 1
            amt_equal = e - s - amt_larger - amt_smaller + 1  # +1 includes the pivot

            if amt_larger >= k:
                return helper(gt_ptr + 1, e, k)

            if amt_equal >= k - amt_larger:
                return pivot

            return helper(s + 1, lt_ptr - 1, k - amt_larger - amt_equal)

        return helper(0, len(nums) - 1, k)
