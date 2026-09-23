'''
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

- We can loop through each array
- Everytime we find a one, DFS on neighbours to verify if its an island
- Repeat for each element in rows
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COLUMN = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        islands = 0

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROW or c == COLUMN or grid[r][c] == "0"):
                return 0            

            # Mark current island as visited
            grid[r][c] = "0"

            for rDir, cDir in dirs:
                dfs(r + rDir, c + cDir)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    islands += 1 
                    dfs(r, c)

        return islands


            