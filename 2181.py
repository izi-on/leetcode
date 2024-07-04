class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        new_tail = new_head
        new_node = ListNode()
        head = head.next
        while head is not None:
            if head.val == 0:
                new_tail.next = new_node
                new_tail = new_node
                new_node = ListNode()
            new_node.val += head.val
            head = head.next
        return new_head.next
