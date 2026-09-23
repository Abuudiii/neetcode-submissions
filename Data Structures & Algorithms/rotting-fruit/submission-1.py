'''
    - track fresh fruits in a hashmap
    - track rotten fruits
    - do a bfs from rotten fruits
        - if surrounding fruit is a fresh fruit then we remove it from the map
    - after q is empty
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROW, COL = len(grid), len(grid[0])
        freshFruit = set()
        q = deque()

        def bfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] != 1:
                return

            grid[r][c] = 2
            freshFruit.remove((r, c))
            q.append([r, c])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    freshFruit.add((r, c))

        minutes = 0
        while freshFruit and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    bfs(r + dr, c + dc)

            minutes += 1

        if len(freshFruit) == 0:
            return minutes
        
        return -1
