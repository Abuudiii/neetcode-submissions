class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        # start from end, count curr sequence length as 1
        # check rest of the right array and track max of just this letter vs me + the right side
        # return dp[0]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums):
                dp[i] = 1
                continue

            currLIS = 1
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    currLIS = max(currLIS, 1 + dp[j])

            dp[i] = currLIS

        return max(dp)