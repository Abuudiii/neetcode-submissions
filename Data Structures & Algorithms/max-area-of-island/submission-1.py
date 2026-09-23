'''
    - loop through array
    - as soon as we find a 1, start dfs and store current area
    - max it with global max
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        ROW, COL = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            total = 1
            for rdir, cdir in dirs:
                total += dfs(r + rdir, c + cdir)
            
            return total


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    currMax = dfs(r, c)
                    area = max(area, currMax)

        return area
        