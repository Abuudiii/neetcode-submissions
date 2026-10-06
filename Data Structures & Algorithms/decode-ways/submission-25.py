class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s) + 1
        dp = [0] * n
        dp[-1] = 1

        '''
            - start from the end
            - dp[i] = num of ways u can decode s from i to end
            - at each i, we can either take it individually or with the next string
            - (1 + dp[i + 1]) + (1 + dp[i + 2])
        '''

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s):
                if s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"):
                    dp[i] += dp[i + 2]

            

            
        return dp[0]