class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in complement:
                return [complement[diff], i]

            complement[nums[i]] = i

        
