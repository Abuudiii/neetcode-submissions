class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
            - push each num to stack
            - when encountering +, add -1 and -2 scores and push result
            - when C, pop from stack
            - when * do -1 * -2
        '''
        stack = []
        
        for elem in operations:
            if elem == "+":
                stack.append(stack[-1] + stack[-2])
            elif elem == "C":
                stack.pop()
            elif elem == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(elem))

        return sum(stack)