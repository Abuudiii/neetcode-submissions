class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [n + 1] * (n + 1)
        dp[1] = 1

        for num in range(2, n + 1):
            if num == n:
                dp[num] = 0
            else:
                dp[num] = num

            for j in range(1, num):
                diff = dp[j] * dp[num - j]
                dp[num] = max(dp[num], diff)

        return dp[-1]