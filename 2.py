# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, ll):
        if ll is None or ll.next is None:
            return ll
        rest = self.reverse(ll.next)
        ll.next.next = ll
        ll.next = None
        return rest

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = ListNode()
        head = sum
        remainder = 0
        while remainder or l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum.next = ListNode(val=(l1_val + l2_val + remainder) % 10)
            remainder = (l1_val + l2_val + remainder) / 10
            sum = sum.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return head.next
