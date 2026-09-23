'''
    - can follow a memoization approach
    - set base case 1 and 0 to return 1
    - then cache the result of each step n into the hashmap
    - recursively call this on both n = f(n - 1) + f(n - 2)
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        cache[1] = 1
        cache[0] = 0

        def recurse(n, cache):
            if n == 0 or n == 1:
                return 1

            if n in cache:
                return cache[n]

            cache[n] = recurse(n - 1, cache) + recurse(n - 2, cache)
            return cache[n]

        recurse(n, cache)

        return cache[n]



