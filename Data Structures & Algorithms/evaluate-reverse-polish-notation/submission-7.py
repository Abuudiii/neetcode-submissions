class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                val = int(stack.pop()) + int(stack.pop())
                stack.append(val)

            elif t == "-":
                a, b = int(stack.pop()), int(stack.pop())
                res = b - a
                stack.append(res)

            elif t == "*":
                res = int(stack.pop()) * int(stack.pop())
                stack.append(res)

            elif t == "/":
                a, b = float(stack.pop()),  float(stack.pop())
                res = b / a
                stack.append(int(res))

            else:
                stack.append(int(t))

        return stack[0]