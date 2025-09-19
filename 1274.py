# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point:
# def __init__(self, x: int, y: int):
# self.x = x
# self.y = y


class Solution:
    def countShips(self, sea: "Sea", topRight: "Point", bottomLeft: "Point") -> int:
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0

        if not sea.hasShips(topRight, bottomLeft):
            return 0

        if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
            return int(sea.hasShips(topRight, bottomLeft))

        is_height_odd = (topRight.y - bottomLeft.y + 1) % 2
        is_width_odd = (topRight.x - bottomLeft.x + 1) % 2

        count_upper_left = self.countShips(
            sea,
            Point(x=(topRight.x + bottomLeft.x) // 2, y=topRight.y),
            Point(x=bottomLeft.x, y=(bottomLeft.y + topRight.y) // 2 + 1),
        )

        count_upper_right = self.countShips(
            sea,
            Point(x=topRight.x, y=topRight.y),
            Point(
                x=(bottomLeft.x + topRight.x) // 2 + 1,
                y=(bottomLeft.y + topRight.y) // 2 + 1 - is_height_odd,
            ),
        )

        count_bottom_left = self.countShips(
            sea,
            Point(
                x=(bottomLeft.x + topRight.x) // 2 - is_width_odd,
                y=(bottomLeft.y + topRight.y) // 2,
            ),
            Point(x=bottomLeft.x, y=bottomLeft.y),
        )

        count_bottom_right = self.countShips(
            sea,
            Point(x=topRight.x, y=(topRight.y + bottomLeft.y) // 2 - is_height_odd),
            Point(
                x=(topRight.x + bottomLeft.x) // 2 + 1 - is_width_odd, y=bottomLeft.y
            ),
        )

        count_middle = 0
        if is_height_odd and is_width_odd:
            count_middle = self.countShips(
                sea,
                Point(
                    x=(topRight.x + bottomLeft.x) // 2,
                    y=(topRight.y + bottomLeft.y) // 2,
                ),
                Point(
                    x=(topRight.x + bottomLeft.x) // 2,
                    y=(topRight.y + bottomLeft.y) // 2,
                ),
            )

        return (
            count_upper_left
            + count_upper_right
            + count_bottom_left
            + count_bottom_right
            + count_middle
        )
