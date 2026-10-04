class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)

            elif t == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)

            elif t == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)

            elif t == "/":
                b, a = float(stack.pop()), float(stack.pop())
                stack.append(int(a / b))

            else:
                stack.append(int(t))

        return stack[0]

