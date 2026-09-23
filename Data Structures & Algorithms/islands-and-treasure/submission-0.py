class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        visited = set()
        ROW, COL = len(grid), len(grid[0])

        def bfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] == -1 or (r, c) in visited:
                return

            visited.add((r, c))
            q.append([r, c])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append([r, c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                for dr, dc in dirs:
                    bfs(r + dr, c + dc)
                
            dist += 1