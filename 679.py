class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ops = ["+", "-", "*", "/"]

        def eval(expr):
            def tree_build(sub_expr):
                if len(sub_expr) == 1:
                    return set([sub_expr[0]])
                new_poss = set()
                for i, c in enumerate(sub_expr):
                    if c not in ops:
                        continue
                    poss_left = tree_build(sub_expr[:i])
                    poss_right = tree_build(sub_expr[i + 1 :])
                    for pl in poss_left:
                        for pr in poss_right:
                            match c:
                                case "+":
                                    new_poss.add(pl + pr)
                                case "-":
                                    new_poss.add(pl - pr)
                                case "*":
                                    new_poss.add(pl * pr)
                                case "/":
                                    if pr != 0:
                                        new_poss.add(pl // pr)
                # print("for", sub_expr, "found", new_poss)
                return new_poss

            psbs = tree_build(expr)
            if 24 in psbs:
                return True
            return False

        def build(nums: list, expr: list):
            for num in nums:
                new_nums = nums.copy()
                new_nums.remove(num)

                expr.append(num)
                if len(expr) == 7:
                    print("trying", expr)
                    res = eval(expr)
                    if res:
                        return True
                else:
                    for op in ops:
                        expr.append(op)
                        if build(new_nums.copy(), expr):
                            return True
                        expr.pop()
                expr.pop()
            return False

        return build(cards, [])
