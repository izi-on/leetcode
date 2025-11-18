class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.end = False


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == len(bits) - 1
