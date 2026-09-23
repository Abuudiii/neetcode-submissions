class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                summedValue = nums[l] + nums[r] + nums[i]

                if summedValue < 0:
                    l += 1

                elif summedValue > 0:
                    r -= 1

                else:
                    triplets.append([nums[l], nums[r], nums[i]])
                    while l < r and nums[l] == nums[l + 1]: l += 1

                    l += 1
                    r -= 1

        return triplets

            