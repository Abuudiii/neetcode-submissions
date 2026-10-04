class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre  = [0] * len(nums)
        suff = [0] * len(nums)
        res  = [0] * len(nums)
        p, s = 1, 1

        for i in range(len(nums)):
            p *= nums[i]
            pre[i] = p

        for i in range(len(nums) - 1, -1, -1):
            s *= nums[i]
            suff[i] = s

        for i in range(len(res)):
            if i == 0:
                res[i] = suff[i + 1]

            elif i == (len(res) - 1):
                res[i] = pre[i - 1]

            else:
                res[i] = pre[i - 1] * suff[i + 1]

        return res

            

