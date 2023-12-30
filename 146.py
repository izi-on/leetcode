class Node:
    @classmethod
    def _remove_node(cls, node):
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

    @classmethod
    def _add_node(cls, insert_after, node):
        tmp = insert_after.next
        tmp.prev = node
        insert_after.next = node
        node.next = tmp
        node.prev = insert_after

    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.count = 0
        self.ll_head = Node()
        self.ll_tail = Node()

        self.ll_head.next = self.ll_tail
        self.ll_tail.prev = self.ll_head

        self.capacity = capacity
        self.hashmap = {}

    def print_ll(self):
        ptr = self.ll_head.next
        while ptr != self.ll_tail:
            print(ptr.val, ptr.key)
            ptr = ptr.next

    def _update_node(self, key, new_val):
        Node._remove_node(self.hashmap[key])
        node = Node(key, new_val)
        Node._add_node(self.ll_tail.prev, node)
        self.hashmap[key] = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap.keys():
            self._update_node(key, self.hashmap[key].val)
            val = self.hashmap[key].val
            print(val)
            return val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap.keys():
            self._update_node(key, value)
            return

        if self.capacity == self.count:
            node_to_remove = self.ll_head.next
            Node._remove_node(node_to_remove)
            del self.hashmap[node_to_remove.key]
            self.count -= 1
        self.count += 1
        new_node = Node(key, value)
        Node._add_node(self.ll_tail.prev, new_node)
        self.hashmap[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
