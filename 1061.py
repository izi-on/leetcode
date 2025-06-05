import string


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        chs = list(string.ascii_lowercase)
        map_to_smallest = {}
        p = [i for i in range(len(chs))]

        def parent(i):
            if i != p[i]:
                p[i] = parent(p[i])
                return p[i]
            return i

        def union(i, j):
            i_p = parent(i)
            j_p = parent(j)
            if i_p != j_p:
                if chs[i_p] < chs[j_p]:
                    p[j_p] = i_p
                else:
                    p[i_p] = j_p

        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord("a"), ord(c2) - ord("a"))
            # print(c1, parent(ord(c1) - ord('a')), c2, parent(ord(c2) - ord('a')))

        # print(list(zip(chs, list(map(lambda x: parent(x), p)))))
        return "".join(list(map(lambda x: chs[parent(ord(x) - ord("a"))], baseStr)))
