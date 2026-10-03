class Solution:
    def numSquares(self, n: int) -> int:
        '''
            - dp[i] represents min number to get to num i
            - at every num, we track the min of all perfect scales to get to num at i
            - e.g num = 4, 
        ''' 

        dp = [n + 1] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            # min perfect squares to get to num at i
            for j in range(1, i + 1):
                if j * j > i:
                    break

                dp[i] = min(dp[i], 1 + dp[i - j * j])
        
        return dp[n]