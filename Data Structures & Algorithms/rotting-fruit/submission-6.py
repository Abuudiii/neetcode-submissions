class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
        fresh = set()
        rotten = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        def bfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or (r, c) not in fresh:
                return

            rotten.append((r, c))
            fresh.remove((r, c))

        minutes = 0
        while rotten:
            for i in range(len(rotten)):
                r, c = rotten.popleft()

                for dr, dc in dirs:
                    bfs(r + dr, c + dc)

            if rotten:
                minutes += 1

        if fresh:
            return -1
        
        return minutes
        