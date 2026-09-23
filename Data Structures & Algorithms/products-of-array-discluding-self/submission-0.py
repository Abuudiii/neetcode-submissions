'''

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)
        res = [0] * len(nums)
        currSum = nums[0]

        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
                continue

            pre[i] = pre[i - 1] * nums[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post[len(nums) - 1] = 1
                continue

            post[i] = post[i + 1] * nums[i + 1]
        
        print(post, pre)

        for i in range(len(nums)):
            res[i] = pre[i] * post[i]

        return res
        