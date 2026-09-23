class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        n = len(nums)

        while l < n:
            if nums[l] == val:
                n -= 1
                nums[l] = nums[n]
            else:
                l += 1
                
        return n
            
        
