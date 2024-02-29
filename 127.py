from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build adj list
        adj_list = defaultdict(list)
        pattern_to_words = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                pattern_to_words[pattern].append(word)
        for words in pattern_to_words.values():
            for word in words:
                for word_to_add in words:
                    if word == word_to_add:
                        continue
                    adj_list[word].append(word_to_add)

        # bfs on adjency list
        bfs = deque()
        bfs.append(beginWord)
        visited = set()
        lvl = 1
        while len(bfs) > 0:
            n = len(bfs)
            for _ in range(n):
                curWord = bfs.popleft()
                if curWord in visited:
                    continue
                visited.add(curWord)
                if curWord == endWord:
                    return lvl
                for neighbour in adj_list[curWord]:
                    bfs.append(neighbour)
            lvl += 1
        return 0
