class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        open_b = []
        unlocked_b = []
        for i in range(len(s)):
            c = s[i]
            if locked[i] == "0":
                unlocked_b.append(i)
            elif c == "(":
                open_b.append(i)
            elif c == ")":
                if open_b:
                    open_b.pop()
                elif unlocked_b:
                    unlocked_b.pop()
                else:
                    return False

        while open_b and unlocked_b and (open_b[-1] < unlocked_b[-1]):
            open_b.pop()
            unlocked_b.pop()

        if open_b:
            return False

        return True
