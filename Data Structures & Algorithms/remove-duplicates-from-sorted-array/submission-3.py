class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] == nums[l + 1]:
                nums.pop(l)
                r -= 1
            elif nums[r] == nums[r - 1]:
                nums.pop(r)
                r -= 1
            else:
                l += 1
                r -= 1
        
        return len(nums)

        


        