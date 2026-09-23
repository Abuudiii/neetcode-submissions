class Solution:
    def isValid(self, s: str) -> bool:
        closingBracket = {']':'[', 
                     ')':'(', 
                     '}':'{'}
        stack = []

        for i in range(len(s)):
            if s[i] not in closingBracket:
                stack.append(s[i])
            
            if s[i] in closingBracket:
                if stack and closingBracket[s[i]] == stack.pop():
                    continue
                else:
                    return False

        if stack:
            return False
        else:
            return True
