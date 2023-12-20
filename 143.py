# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        stack = deque()
        ptr = head
        while ptr:
            stack.append(ptr)
            ptr = ptr.next
        for _ in range(len(stack) // 2):
            tmp = head.next
            head.next = stack.pop()
            head.next.next = tmp
            head = tmp
        head.next = None
