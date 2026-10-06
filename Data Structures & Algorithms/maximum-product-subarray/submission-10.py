class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = max(nums)

        # [-1, 10], 
        # min = -3, max = -3
        # 

        for num in nums:
            if num == 0:
                currMin, currMax = 0, 0
                continue

            tmp = currMax * num
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(tmp, currMin * num, num)

            res = max(res, currMax)

        return res