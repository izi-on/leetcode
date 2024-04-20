class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        marked = set()
        bot_right = [-1, -1]

        def helper(i, j):
            nonlocal bot_right
            if (i, j) in marked:
                return True
            if not (0 <= i < len(land) and 0 <= j < len(land[0])) or land[i][j] == 0:
                return False
            marked.add((i, j))
            print("marked", i, j)
            top = helper(i - 1, j)
            bot = helper(i + 1, j)
            left = helper(i, j - 1)
            right = helper(i, j + 1)
            if not bot and not right:
                print("detected", i, j)
                bot_right = [i, j]
            return True

        rectangles = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if (i, j) not in marked and helper(i, j):
                    print(bot_right)
                    rectangles.append([i, j, bot_right[0], bot_right[1]])
        return rectangles
