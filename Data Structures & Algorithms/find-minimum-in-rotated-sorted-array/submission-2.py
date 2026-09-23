class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]

        for num in nums:
            minVal = min(minVal, num)

        return minVal