p = 0.5
N_max = 10**5


class SkipNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.bottom = None


class Skiplist:
    def __init__(self):
        self.head = SkipNode(-float("inf"))
        self.max_layer = int(math.ceil(log(N_max) / -log(p)))
        self.create_layers(self.head, self.max_layer)

    def create_layers(self, cur_head, layers_left):
        print(layers_left)
        tail = SkipNode(float("inf"))
        cur_head.next = tail
        if layers_left - 1 == 0:
            return
        next_head = SkipNode(float("inf"))
        cur_head.bottom = next_head
        self.create_layers(next_head, layers_left - 1)

    def search(self, target: int) -> bool:
        prevs = self.skip(target)
        return prevs[-1].next.value == target

    def add(self, num: int) -> None:
        prevs = self.skip(num)
        cur_prev_idx = -1
        while -cur_prev_idx != self.max_layer:
            if random.random() > p:
                break
            cur_prev = prevs[cur_prev_idx]
            new_node = SkipNode(num)
            new_node.next = cur_prev.next
            cur_prev.next = new_node
            cur_prev_idx -= 1

    def erase(self, num: int) -> bool:
        prevs = self.skip(target)
        if prevs[-1].next.value != num:
            return False

        cur_prev_idx = -1
        while -cur_prev_idx != len(num) + 1 and prevs[cur_prev_idx].value == nums:
            cur_prev = prevs[cur_prev_idx]
            cur_prev.next = cur_prev.next.next
        return True

    def skip(self, num):
        cur = self.head
        prevs = []
        while cur is not None:
            while cur.next.val < num:
                cur = cur.next
            prevs.append(cur)
            if cur.bottom:
                cur = cur.bottom
        return prevs


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
