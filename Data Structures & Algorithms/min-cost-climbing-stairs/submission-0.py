class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            - start with smaller cost so either 0 or 1
            - at each step 
        '''
        cache = {}
        total = 0

        def dfs(i, cache):
            if i >= len(cost):
                return 0

            if i in cache:
                return cache[i]

            cache[i] = cost[i] + min(dfs(i + 1, cache), dfs(i + 2, cache))
            return cache[i]

        return min(dfs(0, cache), dfs(1, cache))


        