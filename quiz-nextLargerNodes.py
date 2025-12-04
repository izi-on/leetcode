# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        monostack = []
        ans = []
        cur = head
        idx = 0
        while cur:
            while monostack and monostack[-1][0] < cur.val:
                _, i = monostack.pop()
                ans[i] = cur.val
            monostack.append((cur.val, idx))
            cur = cur.next
            idx += 1
            ans.append(0)
        return ans
