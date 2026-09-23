class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROW, COLUMN = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(grid, r, c):
            if min(r, c) < 0 or r == ROW or c == COLUMN or grid[r][c] == "0":
                return 0

            grid[r][c] = "0"

            for dr, dc in dirs:
                dfs(grid, r + dr, c + dc)

        for r in range(ROW):
            for c in range(COLUMN):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(grid, r, c)

        return islands