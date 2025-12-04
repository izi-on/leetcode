class Solution:
    def countCollisions(self, directions: str) -> int:
        moving_r = 0
        stationed = False
        collisions = 0
        for d in directions:
            if d == "L":
                collisions += moving_r
                collisions += bool(stationed or moving_r)
                stationed = stationed or bool(collisions)
                moving_r = 0
            elif d == "S":
                stationed = True
                collisions += moving_r
                moving_r = 0
            elif d == "R":
                moving_r += 1
        return collisions
