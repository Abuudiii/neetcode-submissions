class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        '''
            - recursively:
                - can either go down or right  at each cell[r][c]
                - at each cell our paths will be how many number of ways u can get to r + 1 + c + 1
                - we can cache each cell to avoid recomputation
                - return 1 at basecase and 0 for out of bounds
        '''

        grid = [[0] * n for _ in range(m)]
        
        def dfs(r, c):
            # out of bounds check
            if r == m or c == n:
                return 0

            # avoiding recomputation
            if grid[r][c] != 0:
                return grid[r][c]

            # reached target
            if r == m - 1 and c == n - 1:
                return 1

            grid[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return grid[r][c]

        dfs(0, 0)
        return grid[0][0]
