class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return
        map_og_to_new = {}
        cur_head = head
        while cur_head is not None:
            new_node = Node(cur_head.val)
            map_og_to_new[cur_head] = new_node
            cur_head = cur_head.next

        cur_head = head
        while cur_head is not None:
            nn = map_og_to_new[cur_head]
            nnext = map_og_to_new[cur_head.next] if cur_head.next else None
            nrandom = map_og_to_new[cur_head.random] if cur_head.random else None
            nn.next = nnext
            nn.random = nrandom
            cur_head = cur_head.next
        return map_og_to_new[head]
