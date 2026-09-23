class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(heights), len(heights[0])
        pac = set()
        atl = set()
        res = []

        def dfs(r, c, prev, visited):
            if min(r, c) < 0 or r == ROW or c == COL or heights[r][c] < prev or (r, c) in visited:
                return

            visited.add((r, c))

            for dr, dc in dirs:
                dfs(r + dr, c + dc, heights[r][c], visited)

        
        for c in range(COL):
            dfs(0, c, heights[0][c], pac)
            dfs(ROW - 1, c, heights[ROW - 1][c], atl)

        for r in range(ROW):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COL - 1, heights[r][COL - 1], atl)

        for r in range(ROW):
            for c in range(COL):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res

        