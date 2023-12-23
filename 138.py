"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        nodes = [Node(0)]
        rnd_idx = {}
        while head is not None:
            rnd_idx[head] = len(nodes) - 1
            new_node = Node(head.val, head.next, random=head.random)
            nodes[-1].next = new_node
            nodes.append(new_node)
            head = head.next
        nodes = nodes[1:]
        for _, node in enumerate(nodes):
            # print(rnd_idx[node.random])
            idx = rnd_idx.get(node.random, None)
            node.random = nodes[idx] if idx is not None else None
        return nodes[0]
