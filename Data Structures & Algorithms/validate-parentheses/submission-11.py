class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openMap = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }

        for c in s:
            if c in openMap.keys():
                stack.append(c)
                continue
            
            if not stack:
                return False

            curr = stack.pop()

            if c != openMap[curr]:
                return False 

        return True if not stack else False