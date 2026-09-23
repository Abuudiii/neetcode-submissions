class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = deque()
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] != 1:
                return

            grid[r][c] = 2
            fresh.remove((r, c))
            rotten.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
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
