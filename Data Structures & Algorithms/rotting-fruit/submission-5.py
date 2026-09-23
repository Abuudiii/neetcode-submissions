class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = set()
        ROW, COL =  len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    q.append((r, c))

        def bfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or (r, c) not in fresh:
                return

            fresh.remove((r, c))
            q.append((r, c))


        minutes = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    bfs(dr + r, dc + c)

            if q:
                minutes += 1

        return minutes if len(fresh) == 0 else -1
