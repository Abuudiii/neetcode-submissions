class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        amount = [0] * len(nums)
        amount[0] = nums[0]
        amount[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            amount[i] = max((nums[i] + amount[i - 2]),amount[i - 1])

        return amount[-1]