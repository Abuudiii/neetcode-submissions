class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        res = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
                continue

            prefix[i] = nums[i] * prefix[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = nums[i]
                continue
            
            suffix[i] = nums[i] * suffix[i + 1]

        for i in range(len(nums)):
            if i == 0:
                res[i] = suffix[i + 1]

            elif i + 1 < len(nums) and i - 1 >= 0:
                res[i] = prefix[i - 1] * suffix[i + 1]

            elif i == (len(nums) - 1):
                res[i] = prefix[i - 1]

        return res



            