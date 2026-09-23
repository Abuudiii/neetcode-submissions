'''
    - top down:
        - can either go down or right  at each cell[r][c]
        - at each cell our paths will be how many number of ways u can get to r + 1 + c + 1
        - we can cache each cell to avoid recomputation
        - return 1 at basecase and 0 for out of bounds
    
    - bottom up:
        - initially have a fake r + 1 row with just 0s
        - at each iteration update prevRow to be currRow and create a new blank currRow
        - start at target initally
        - at each index the ways to get to target will be the ways to get to curr[c + 1] + prevRow[c]
        - return prevRow[0]
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            currRow = [0] * n
            currRow[n - 1] = 1

            for c in range(n - 2, -1, -1):
                currRow[c] = currRow[c + 1] + prevRow[c]

            prevRow = currRow

        return prevRow[0]