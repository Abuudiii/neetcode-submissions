class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            curr = i
            for num in range(1, i):
                if num * num > i:
                    break

                curr = min(curr, 1 + dp[i - num * num])
            dp[i] = curr
                
        return dp[n]