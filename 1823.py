class Node:
    def __init__(self, val: int, next_n: "Node | None" = None):
        self.val = val
        self.next_n = next_n


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # build the linked list
        cur_node = Node(val=1)
        first_n = cur_node
        for i in range(2, n + 1):
            new_node = Node(val=i)
            cur_node.next_n = new_node
            cur_node = new_node
        cur_node.next_n = first_n
        prev_node = cur_node
        cur_node = first_n

        # traverse
        while cur_node.next_n != cur_node:
            for _ in range(k - 1):
                prev_node = cur_node
                cur_node = cur_node.next_n
            prev_node.next_n = cur_node.next_n
            cur_node = cur_node.next_n

        return cur_node.val
