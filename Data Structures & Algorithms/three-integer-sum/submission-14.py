class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + nums[i]

                if total < 0:
                    l += 1

                elif total > 0:
                    r -= 1

                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res