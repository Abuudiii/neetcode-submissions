class Solution:
    def tribonacci(self, n: int) -> int:
        # t0 = 0, t1 = 1, t2 = 1
        # tn = tn - 1, tn - 2, tn - 3
        '''
            - we could have base cases defined
            - recurse down to base case then bubble up answer and return it
        '''
        if n <= 2:
            return 1 if n != 0 else 0

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]