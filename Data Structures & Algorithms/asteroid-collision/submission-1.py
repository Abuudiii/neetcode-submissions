class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
            - push to stack
            - when encountering an oppsite size astroid, crash them and push value accordingly
        '''
        stack = []

        # [2, ]
        for a in asteroids:
            survived = True
            while stack and stack[-1] > 0 and a < 0 and survived:
                prev = stack.pop()
                curr = abs(a)

                if curr > prev:
                    continue
                elif prev > curr:
                    survived = False
                    stack.append(prev)
                elif prev == curr:
                    survived = False
            
            if survived:
                stack.append(a)

        return stack