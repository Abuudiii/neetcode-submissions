class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {len(nums) : 0}

        def dfs(i):
            if i in cache:
                return cache[i]

            longest = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    longest = max(longest, 1 + dfs(j))

            cache[i] = longest
            return cache[i]

        for i in range(len(nums)):
            dfs(i)

        return max(cache.values())
            
