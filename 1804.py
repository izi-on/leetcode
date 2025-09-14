class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.count_word_end = 0  # count the amount of words that end on this node
        self.children = {}

    def get_children(self):
        return self.children.values()

    def get_child(self, value):
        return self.children.get(value, None)

    def add_child(self, value):
        self.children[value] = TrieNode(value)

    def remove_child(self, value):
        del self.children[value]

    def add_child_if_not_present_and_return_child_node(self, value):
        if not self.get_child(value):
            self.add_child(value)
        return self.get_child(value)

    def mark_end(self):
        self.count_word_end += 1

    def unmark_end(self):
        self.count_word_end -= 1

    def end_count(self):
        return self.count_word_end


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for chr in word:
            current_node.add_child_if_not_present_and_return_child_node(chr)
        current_node.mark_end()

    def countWordsEqualTo(self, word: str) -> int:
        destination_node = self.traverse_trie(self.root, word)
        if destination_node is None:
            return 0
        return destination_node.end_count()

    def countWordsStartingWith(self, prefix: str) -> int:
        count_prefixed_words = 0

        def dfs(current_node):
            nonlocal count_prefixed_words
            if current_node is None:
                return
            count_prefixed_words += current_node.end_count()
            for child_node in current_node.get_children():
                dfs(child_node)

        destination_node = self.traverse_trie(self.root, prefix)
        if destination_node is None:
            return 0
        dfs(destination_node)
        return count_prefixed_words

    def erase(self, word: str) -> None:
        def dfs(current_node, word_idx):
            if current_node is None:
                return

            if word_idx == len(word):
                current_node.unmark_end()
            elif dfs(current_node.get_child(word[word_idx]), word_idx + 1):
                current_node.remove_child(word[word_idx])

            if current_node.end_count == 0 and len(current_node.get_children()):
                return True

        dfs(self.root, 0)

    def traverse_trie(self, start_node, word):
        current_node = start_node
        for chr in word:
            current_node = current_node.get_child(chr)
            if current_node is None:
                return None
        return current_node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
