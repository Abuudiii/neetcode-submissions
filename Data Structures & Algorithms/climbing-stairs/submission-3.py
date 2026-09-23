class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            - base cases: n == 1 or n == 2, return whatever n is
            - 
        '''

        cache = {}

        def dp(n, cache):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            elif n in cache:
                return cache[n]

            cache[n] = dp(n - 1, cache) + dp(n - 2, cache)
            return cache[n]

        return dp(n, cache)