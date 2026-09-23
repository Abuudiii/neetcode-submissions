class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
            - keep moving r until sum >= target
            - while sum >= target, keep moving left to track and update minimum size
            - return minimum size
            - if whole array is iterated over and target isnt reaches return 0
        '''

        if sum(nums) < target:
            return 0

        l = 0
        minSub = math.inf
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                minSub = min(minSub, (r - l + 1))
                total -= nums[l]
                l += 1

        return minSub