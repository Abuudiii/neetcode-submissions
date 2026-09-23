class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, numList, cache):
            if i >= len(numList):
                return 0
            
            if i in cache:
                return cache[i]

            cache[i] = max(dfs(i + 1, numList, cache), numList[i] + dfs(i + 2, numList, cache))
            return cache[i]

        return max(nums[0], dfs(0, nums[1:], {}), dfs(0, nums[:-1], {}))
