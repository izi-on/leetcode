from collections import defaultdict
from functools import reduce


class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        map_language_set = defaultdict(set)
        for i, language in enumerate(languages):
            map_language_set[i] = set(language)

        unconnected_friends = set()
        for friendship in friendships:
            u, v = friendship
            if len(map_language_set[u - 1].intersection(map_language_set[v - 1])) != 0:
                continue
            unconnected_friends.add(u)
            unconnected_friends.add(v)

        max_lang_count = -1
        lang_count = defaultdict(int)
        for friend in unconnected_friends:
            for lang in map_language_set[friend - 1]:
                lang_count[lang] += 1
                max_lang_count = max(max_lang_count, lang_count[lang])

        return len(unconnected_friends) - max_lang_count
