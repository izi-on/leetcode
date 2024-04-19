from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        queue = deque([i for i in range(len(deck))])
        new_deck = [0] * len(deck)
        switch = True
        ptr = 0
        while queue:
            if switch:
                new_deck[queue.popleft()] = deck[ptr]
                ptr += 1
            else:
                queue.append(queue.popleft())
            switch = not switch
        return new_deck
