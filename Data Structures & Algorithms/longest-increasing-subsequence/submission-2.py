class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        for i in range(len(nums)):
            longest = 1

            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    longest = max(longest, 1 + dp[j])

            dp[i] = longest

        return max(dp)
        