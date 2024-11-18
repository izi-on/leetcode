from collections import defaultdict


class Node:
    def __init__(self, key: int = 0, val: set = set(), start=False):
        self.key = key  # freq
        self.strs = val  # list of keys
        self.prev: Node | None = None
        self.next: Node | None = None
        self.start = start

    def is_empty(self):
        return len(self.strs) == 0


class AllOne:
    def __init__(self):
        self.head = Node(0, start=True)
        self.tail = self.head
        self.position = {}
        self.max_node: Node | None = None

    def remove_node(self, node: Node):
        print("removing node", node.key)
        prev = node.prev
        next = node.next
        if prev:
            print("prev", prev.key)
            prev.next = next
        if next:
            print("next", next.key)
            next.prev = prev

    def add_node(self, node: Node, prev: Node):
        next = prev.next
        prev.next = node
        node.next = next
        node.prev = prev
        if next:
            next.prev = node

    def move_to_node(self, key: str, node1: "Node", node2: "Node"):
        node1.strs.remove(key)
        node2.strs.add(key)
        if node1.is_empty() and not node1.start:
            self.remove_node(node1)

    def inc(self, key: str) -> None:
        if key not in self.position:  # edge case when the key isnt set
            self.position[key] = self.head
            self.head.strs.add(key)
        freq_node = self.position[key]
        cur_node = None

        # case 1: no next node
        if freq_node.next is None:
            new_node = Node(freq_node.key + 1, set([key]))
            self.add_node(new_node, freq_node)
            self.move_to_node(key, freq_node, new_node)
            self.position[key] = new_node
            cur_node = new_node

        # case 2: next node, but not by increment of 1
        elif freq_node.next.key != freq_node.key + 1:
            new_node = Node(freq_node.key + 1, set([key]))
            self.add_node(new_node, freq_node)
            self.move_to_node(key, freq_node, new_node)
            self.position[key] = new_node
            cur_node = new_node

        # case 3: next node exists and is by increment of 1
        elif freq_node.next.key == freq_node.key + 1:
            self.move_to_node(key, freq_node, freq_node.next)
            self.position[key] = freq_node.next
            cur_node = freq_node.next

        if cur_node is None:
            raise Exception("cur_node is None")

        # update new max node if necessary
        if self.max_node is None:
            self.max_node = cur_node
        elif self.max_node.key < cur_node.key:
            self.max_node = cur_node

    def dec(self, key: str) -> None:
        if key not in self.position:
            return
        freq_node = self.position[key]
        cur_node = None

        # case 1: prev node, but not by decrement of 1
        if freq_node.prev.key != freq_node.key - 1:
            new_node = Node(freq_node.key - 1, set([key]))
            self.add_node(new_node, freq_node.prev)
            self.move_to_node(key, freq_node, new_node)
            self.position[key] = new_node
            cur_node = new_node

        # case 2: prev node exists and is by decrement of 1
        elif freq_node.prev.key == freq_node.key - 1:
            self.move_to_node(key, freq_node, freq_node.prev)
            self.position[key] = freq_node.prev
            cur_node = freq_node.prev

        if cur_node is None:
            raise Exception("cur_node is None on dec")

        # update max node if necessary
        if self.max_node is freq_node and freq_node.is_empty():
            if cur_node is not self.head:
                self.max_node = cur_node
            else:
                self.max_node = None

        # remove key if necessary
        if cur_node is self.head:
            del self.position[key]

    def getMaxKey(self) -> str:
        print(self.max_node)
        if self.max_node is not None:
            print(self.max_node.strs)
            return list(self.max_node.strs)[0]
        return ""

    def getMinKey(self) -> str:
        if self.head.next is not None:
            return list(self.head.next.strs)[0]
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
