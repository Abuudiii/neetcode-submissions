class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}

        # target depends on target - 1, target - 2, so on
        # at each target value lesser than target, find the ways u can sum up to that
        def dfs(target):
            if target in cache:
                return cache[target]

            if target < 0:
                return 0
            
            if target == 0:
                return 1

            res = 0
            for num in nums:
                res += dfs(target - num)

            cache[target] = res
            return cache[target]

        return dfs(target)