from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        num_of_groups = len(hand) // groupSize
        hand = sorted(hand)
        groups = defaultdict(list)
        group_count = 0
        for h in hand:
            # print("at ", h)
            if len(groups[h - 1]) == 0:
                # print("making new group")
                if group_count == num_of_groups:
                    return False
                group_count += 1
                groups[h].append(1)
            else:
                # print("adding to group: ", groups[h - 1])
                num_in_group = groups[h - 1].pop()
                if num_in_group + 1 != groupSize:
                    groups[h].append(num_in_group + 1)
        return True
