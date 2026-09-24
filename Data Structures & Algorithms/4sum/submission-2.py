class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l, r = 0, 1
        nums.sort()
        res = []

        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l - 1]:
                continue

            for r in range(l + 1, len(nums)):
                if r - l > 1 and nums[r] == nums[r - 1]:
                    continue

                L, R = r + 1, len(nums) - 1
                while L < R:
                    total = nums[l] + nums[r] + nums[L] + nums[R]

                    if total > target:
                        R -= 1
                    elif total < target:
                        L += 1
                    else:
                        res.append([nums[l], nums[r], nums[L], nums[R]])
                        L += 1
                        R -= 1

                        while L < R and nums[L] == nums[L - 1]:
                            L += 1
                        while L < R and nums[R] == nums[R + 1]:
                            R -= 1

        return res