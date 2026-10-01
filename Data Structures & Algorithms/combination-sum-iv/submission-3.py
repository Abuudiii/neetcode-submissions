class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(num):
            if num > target:
                return 0

            if num == target:
                return 1

            if num in cache:
                return cache[num]

            curr = 0
            for n in nums:
                curr += dfs(num + n)

            cache[num] = curr
            return cache[num]

        count = 0
        for num in nums:
            count += dfs(num)

        return count