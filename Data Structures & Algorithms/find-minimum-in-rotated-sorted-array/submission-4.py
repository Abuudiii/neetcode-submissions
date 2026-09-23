class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = 0

        while l < r:
            middle = l + (r - l) // 2
            if nums[middle] < nums[r]:
                r = middle
            else:
                l = middle + 1

        return nums[l]
