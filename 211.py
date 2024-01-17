class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_word_end = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        ptr = self.root
        idx = 0
        while idx != len(word):
            track_parent = ptr
            ptr = ptr.children.get(word[idx])
            if not ptr:
                node = Node(word[idx])
                track_parent.children[word[idx]] = node
                ptr = node
            idx += 1
        ptr.is_word_end = True

    def search(self, word: str) -> bool:
        def dfs(root, idx):
            ptr = root
            while idx != len(word):
                if word[idx] == ".":
                    for child in ptr.children.values():
                        if dfs(child, idx + 1):
                            return True
                    return False
                ptr = ptr.children.get(word[idx])
                if not ptr:
                    return False
                idx += 1
            return ptr.is_word_end

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
