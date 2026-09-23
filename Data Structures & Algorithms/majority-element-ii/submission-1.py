class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numCount = {}
        n = len(nums)
        
        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        ans = []
        for key, value in numCount.items():
            if value > (n / 3):
                ans.append(key)

        return ans
