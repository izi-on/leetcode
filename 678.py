class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = 0
        left_max = 0
        for c in s:
            match c:
                case "(":
                    left_min += 1
                    left_max += 1
                case ")":
                    left_min -= 1
                    left_max -= 1
                    if left_max < 0:
                        return False
                case "*":
                    left_min = max(0, left_min - 1)
                    left_max += 1
        return left_min == 0
