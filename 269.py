from collections import defaultdict
import string


class Loop(Exception):
    pass


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def find_order(a, b):
            for i in range(min(len(a), len(b))):
                c_a = a[i]
                c_b = b[i]
                if c_a == c_b:
                    continue
                return (c_a, c_b)
            if len(a) > len(b):
                raise Loop
            return None

        def topo_sort(cur_chars):
            if len(cur_chars) == 0:
                return ""
            next_gen = set()
            for cur_char in cur_chars:
                for next_char in adj_list[cur_char]:
                    rev_adj_list[next_char].remove(cur_char)
                    if len(rev_adj_list[next_char]) == 0:
                        next_gen.add(next_char)
            return "".join(list(cur_chars)) + topo_sort(next_gen)

        def detect_cycle(c, visited, finished):
            print("start " + c)
            if c in visited:
                print("cycle detected: " + c)
                raise Loop
            if c in finished:
                return
            visited.add(c)
            for n_c in adj_list[c]:
                detect_cycle(n_c, visited, finished)
            visited.remove(c)
            finished.add(c)
            print("end " + c)

        adj_list = defaultdict(set)
        rev_adj_list = defaultdict(set)
        sinks = set([c for word in words for c in word])

        try:
            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    word_a = words[i]
                    word_b = words[j]
                    res = find_order(word_a, word_b)
                    if not res:
                        continue
                    c_a, c_b = res
                    if c_b in sinks:
                        sinks.remove(c_b)
                    adj_list[c_a].add(c_b)
                    rev_adj_list[c_b].add(c_a)

            for c in string.ascii_lowercase:
                detect_cycle(c, set(), set())
            return topo_sort(sinks)
        except Loop:
            return ""
