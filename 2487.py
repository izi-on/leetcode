# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        track_head = head

        def helper(node, prev):
            nonlocal track_head
            if node is None:
                return 0
            max_right = helper(node.next, node)
            if node.val < max_right:
                if prev is None:
                    track_head = node.next
                else:
                    prev.next = node.next
            return max(max_right, node.val)

        helper(track_head, None)
        return track_head
