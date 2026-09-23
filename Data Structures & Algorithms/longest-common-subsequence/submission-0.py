class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r, c = len(text1) + 1,  len(text2) + 1
        dp = [[0] * c for _ in range(r)]

        for i in range(1, r):
            for j in range(1, c):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                elif text1[i - 1] != text2[j - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[r - 1][c - 1]