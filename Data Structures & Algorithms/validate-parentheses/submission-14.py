class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        # stack = [(, [, {, }, ], )]
        '''
            - keep pushing opening brackets to stack
            - when encountering closed bracket, pop top of stack and compare
            - if same, continue to next,
            - else return False
            - return True if list is iterated over and stack is empty
        '''

        stack = []

        for i in range(len(s)):
            if stack and s[i] in mappings:
                if stack[-1] == mappings[s[i]]:
                    stack.pop()
                    continue
                else:
                    return False

            stack.append(s[i])

        if stack:
            return False

        return True
