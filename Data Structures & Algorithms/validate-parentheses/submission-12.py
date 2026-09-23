class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { "(" : ")", "[" : "]", "{" : "}" }

        for c in s:
            if c in closeToOpen:
                stack.append(c)
                continue

            if not stack:
                return False

            curr = stack.pop()

            if c != closeToOpen[curr]:
                return False

        return True if not stack else False