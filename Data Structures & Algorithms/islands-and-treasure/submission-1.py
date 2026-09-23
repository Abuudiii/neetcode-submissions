class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            - go through the list and find all treasures
            - start a bfs from each treasure and keep going and updating each land tile
        '''
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        visited = set()

        def bfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] != INF or (r, c) in visited:
                return

            visited.add((r, c))
            q.append((r, c))      

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in dirs:
                    bfs(r + dr, c + dc)

            dist += 1

