# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ptr = head
        track_head = ListNode()
        track_start = track_head
        next_head = track_head
        while ptr is not None:
            count = 1
            track_tail = ptr
            while count != k and ptr.next is not None:
                ptr = ptr.next
                count += 1
            if count != k:
                return track_start.next
            next_head = ptr.next
            _, track_head.next = self.reverse(track_tail, count - 1)
            track_head = track_tail
            ptr = next_head
            track_tail.next = ptr
        return track_start.next

    def print_ll(self, head):
        ptr = head
        while ptr:
            print(ptr)
            ptr = ptr.next

    def reverse(self, head, left):
        if not left or not head or head.next is None:
            if not head:
                return 0, None
            else:
                head.next = None
                return 1, head

        count, rl = self.reverse(head.next, left - 1)
        head.next.next = head
        head.next = None
        return count + 1, rl
