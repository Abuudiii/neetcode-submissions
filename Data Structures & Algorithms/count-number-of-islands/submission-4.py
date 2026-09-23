class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROW, COL = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] != "1":
                return

            grid[r][c] = 0
            
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands
