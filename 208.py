class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.word_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        idx = 0
        while ptr is not None and idx != len(word):
            ptr_track = ptr
            ptr = ptr.children.get(word[idx], None)
            if not ptr:
                node = Node(word[idx])
                ptr_track.children[word[idx]] = node
                ptr = node
            idx += 1
        if ptr and idx == len(word):
            ptr.word_end = True

    def search(self, word: str) -> bool:
        ptr = self.root
        idx = 0
        while ptr is not None and idx != len(word):
            ptr = ptr.children.get(word[idx], None)
            idx += 1
        if ptr and idx == len(word) and ptr.word_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        idx = 0
        while ptr is not None and idx != len(prefix):
            ptr = ptr.children.get(prefix[idx], None)
            idx += 1
        if ptr and idx == len(prefix):
            return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
