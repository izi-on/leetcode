class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def find_cut(starts_or_ends):
            overlapping = set()
            count_cut = 0
            starts_or_ends = sorted(starts_or_ends)
            for se in starts_or_ends:
                (
                    _,
                    is_start,
                    rectangle,
                ) = se
                if not is_start:
                    overlapping.remove(rectangle)
                    if not overlapping:
                        count_cut += 1
                        if count_cut == 3:
                            return True
                else:
                    overlapping.add(rectangle)
            return False

        # for vertical
        verticals = []
        for i, rectangle in enumerate(rectangles):
            verticals.append((rectangle[1], True, i))
            verticals.append((rectangle[3], False, i))
        # for horizontal
        horizontal = []
        for i, rectangle in enumerate(rectangles):
            horizontal.append((rectangle[0], True, i))
            horizontal.append((rectangle[2], False, i))
        return find_cut(verticals) or find_cut(horizontal)
