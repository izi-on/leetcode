class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                match t:
                    case "+":
                        stack.append(n1 + n2)
                    case "-":
                        stack.append(n1 - n2)
                    case "*":
                        stack.append(n1 * n2)
                    case "/":
                        stack.append(int(n1 / n2))
        return stack[-1]
