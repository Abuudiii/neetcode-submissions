class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        preSum = {0 : 1}

        for num in nums:
            currSum += num
            diff = currSum - k

            if diff in preSum:
                res += preSum[diff]

            preSum[currSum] = 1 + preSum.get(currSum, 0)

        return res