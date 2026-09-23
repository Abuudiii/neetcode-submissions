'''
    - do ds from all border nodes
    - pass in appropriate hashset
    - in the end, return all common nodes
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        atl = set()
        pac = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visited, prevVal):
            if min(r, c) < 0 or r == ROW or c == COL or heights[r][c] < prevVal or (r, c) in visited:
                return

            visited.add((r, c))

            for dr, dc in dirs:
                dfs(r + dr, c + dc, visited, heights[r][c])
            
        
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL - 1, atl, heights[r][COL - 1])
        
        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW - 1, c, atl, heights[ROW - 1][c])

        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res



