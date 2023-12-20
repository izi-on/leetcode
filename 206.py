# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.new_head = None

    def reverseList(self, head):
        self.reverse(head)
        return self.new_head

    def reverse(self, head):
        if not head or not head.next:
            self.new_head = head
            return head

        head.next = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return head
