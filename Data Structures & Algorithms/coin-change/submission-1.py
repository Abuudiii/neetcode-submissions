class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(curr):
            if curr == 0:
                return 0
            
            if curr < 0:
                return math.inf
            
            if curr in cache:
                return cache[curr]

            minCoins = math.inf
            for num in coins:
                minCoins = min(1 + dfs(curr - num), minCoins)

            cache[curr] = minCoins
            return cache[curr]

        res = dfs(amount)

        if res != math.inf:
            return res
        else:
            return -1



            