class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = set()
        ROW, COL = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        def bfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or (r, c) not in fresh:
                return

            fresh.remove((r, c))
            rotten.append((r, c))

        time = 0
        while rotten:
            for i in range(len(rotten)):
                r, c = rotten.popleft()

                for dr, dc in dirs:
                    bfs(r + dr, c + dc)

            if rotten:
                time += 1

        if fresh:
            return -1

        return time