class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        final = []
        spaces = set(spaces)
        for i, c in enumerate(s):
            if i in spaces:
                final.append(" " + c)
                continue
            final.append(c)
        return "".join(final)
