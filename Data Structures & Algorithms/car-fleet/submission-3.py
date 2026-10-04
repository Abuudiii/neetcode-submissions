class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            - push all p and s to a stack
            - start with last car
            - for each car, check its arrival time vs last car
            - if its lesser, skip this since itll join the fleet
            - otherwise push it back to stack
            - in the end stack length is num of fleets
        '''

        stack = []
        res = []
        pairs = sorted(zip(position, speed))

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)

        while stack:
            if not res:
                res.append(stack.pop())
                continue

            time = stack.pop()
            if time > res[-1]:
                res.append(time)
            
        return len(res)
            
            