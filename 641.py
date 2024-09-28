from typing import Union


class Node:
    value: int | None
    next: Union["Node", None]
    prev: Union["Node", None]

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    @staticmethod
    def connect(node_a: "Node", node_b: "Node"):
        node_a.next = node_b
        node_b.prev = node_a


class MyCircularDeque:
    head: Node
    tail: Node
    k: int
    count: int

    def __init__(self, k: int):
        self.head = Node(None)
        self.tail = Node(None)
        self.k = k
        self.count = 0
        Node.connect(self.head, self.tail)

    def insertFront(self, value: int) -> bool:
        assert self.head.next is not None
        if self.isFull():
            return True
        new_node = Node(value)
        Node.connect(new_node, self.head.next)
        Node.connect(self.head, new_node)
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        assert self.tail.prev is not None
        if self.isFull():
            return False
        new_node = Node(value)
        Node.connect(self.tail.prev, new_node)
        Node.connect(new_node, self.tail)
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        try:
            assert self.head.next is not None
            assert self.head.next.next is not None
        except AssertionError:
            return False
        Node.connect(self.head, self.head.next.next)
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        try:
            assert self.tail.prev is not None
            assert self.tail.prev.prev is not None
        except AssertionError:
            return False
        Node.connect(self.tail.prev.prev, self.tail)
        self.count -= 1
        return True

    def getFront(self) -> int:
        try:
            assert self.head.next is not None
            assert self.head.next.value is not None
        except AssertionError:
            return -1

        return self.head.next.value

    def getRear(self) -> int:
        try:
            assert self.tail.prev is not None
            assert self.tail.prev.value is not None
        except AssertionError:
            return -1
        return self.tail.prev.value

    def isEmpty(self) -> bool:
        return self.head.next is self.tail

    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
