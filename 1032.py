from collections import defaultdict


class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.is_end = False


class StreamChecker:
    def insert_word_in_trie(self, word: str):
        current_node = self.root
        for c in word:
            if c not in current_node.children.keys():
                new_node = TrieNode(c)
                current_node.children[c] = new_node
            current_node = current_node.children[c]
        current_node.is_end = True

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.possible_current_nodes = [self.root]
        for word in words:
            self.insert_word_in_trie(word)

    def check_if_suffix(self):
        return any([node.is_end for node in self.possible_current_nodes])

    def query(self, letter: str) -> bool:
        new_possible_current_nodes = [self.root]
        for node in self.possible_current_nodes:
            if letter in node.children.keys():
                new_possible_current_nodes.append(node.children[letter])
        self.possible_current_nodes = new_possible_current_nodes
        return self.check_if_suffix()


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
