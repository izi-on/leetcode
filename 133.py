class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        def helper(node, map_to_new):
            if not node:
                return None
            if node in map_to_new.keys():
                return map_to_new[node]
            new_node = Node()
            map_to_new[node] = new_node
            new_neighbors = []
            for neighbor in node.neighbors:
                new_neighbor = helper(neighbor, map_to_new)
                print(f"node {node} added {new_neighbor}")
                new_neighbors.append(new_neighbor)
            new_node.val = node.val
            new_node.neighbors = new_neighbors
            return new_node

        return helper(node, {})
