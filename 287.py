class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = nums[0], nums[0]
        head = slow

        def next(val):
            return nums[val]

        while fast and next(fast):
            fast = next(next(fast))
            slow = next(slow)
            if fast == slow:
                break

        while head != slow:
            head = next(head)
            slow = next(slow)

        return slow
