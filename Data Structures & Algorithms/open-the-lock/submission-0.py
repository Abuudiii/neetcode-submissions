class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
            - need to avoid deadlock combinations
            - need to find min num of rotations to get to target
            - bfs layer, at each iteration we turn the lock and keep track of turns
            - if next turn causes deadlock, maybe skip it and turn the other ones
            - once we hit the target, track it in the minimum
        '''
        dead = set(deadends)
        if "0000" in dead:
            return -1
        visited = set()
        q = deque()

        def bfs(code):
            res = []
            for i in range(4):
                digit = int(code[i])
                for turn in [-1, 1]:
                    newDigit = (digit + turn) % 10
                    new = code[:i] + str(newDigit) + code[i+1:]
                    res.append(new)

            return res

        q.append(("0000", 0))
        visited.add("0000")

        while q:
            code, turns = q.popleft()

            if code == target:
                return turns
            
            combos = bfs(code)
            for c in combos:
                if c in dead or c in visited:
                    continue
                else:
                    q.append((c, turns + 1))
                    visited.add(c)
        
        return -1

