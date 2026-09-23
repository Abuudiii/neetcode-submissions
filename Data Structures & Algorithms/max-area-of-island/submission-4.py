class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] != 1:
                return 0

            count = 1
            grid[r][c] = 0

            for dr, dc in dirs:
                count += dfs(r + dr, c + dc)

            return count

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea