# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return rest

    def removeNthFromEnd(self, head, n):
        rev_head = self.reverse(head)
        if n == 1:
            return self.reverse(rev_head.next)
        prev = None
        nxt = ListNode(next=rev_head)
        for _ in range(n):
            prev = nxt
            nxt = nxt.next
        print(prev.val, nxt.val)
        prev.next = nxt.next
        return self.reverse(rev_head)
