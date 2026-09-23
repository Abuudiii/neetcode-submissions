class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)
        ans[:len(nums)] = nums

        l = 0
        r = len(nums)

        for r in range(len(nums), len(ans), 1):
            ans[r] = nums[l]
            l += 1

        return ans  

        
