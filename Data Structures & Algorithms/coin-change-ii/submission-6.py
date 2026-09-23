class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
            - core logic of coin change one used
            - recurse on number
            - maybe a 2d grid where each grids value can depend on a subproblem of its adjacent grids
            - bubble up answer to grid[0][0]

            [0, 0, 0, 0]
            [0, 0, 0, 0]
            [0, 0, 0, 0]
        '''
        r, c  = len(coins), amount + 1
        dp = [[0] * c for _ in range(r)]

        for i in range(r):
            dp[i][0] = 1

        for j in range(1, c):
            dp[0][j] = 1 if j % coins[0] == 0 else 0
        

        for i in range(1, r):
            for a in range(1, c):
                prevCoin = dp[i - 1][a] if i - 1 >= 0 else 0
                prevCombo = dp[i][a - coins[i]] if a >= coins[i] else 0

                dp[i][a] =  prevCoin + prevCombo

        return dp[r - 1][amount]

