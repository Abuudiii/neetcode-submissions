class Solution:
    def tribonacci(self, n: int) -> int:
        # t0 = 0, t1 = 1, t2 = 1
        # tn = tn - 1, tn - 2, tn - 3
        '''
            - we could have base cases defined
            - recurse down to base case then bubble up answer and return it
        '''
        cache = {}
        cache[0] = 0
        cache[1] = 1
        cache[2] = 1

        def dfs(n):
            if n < 0:
                return 0

            if n in cache:
                return cache[n]

            cache[n] = dfs(n - 1) + dfs(n - 2) + dfs(n - 3)
            return cache[n]

        return dfs(n)