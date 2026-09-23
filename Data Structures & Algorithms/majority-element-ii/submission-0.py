class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numCount = {}
        n = len(nums)
        
        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        sorted_D = dict(sorted(numCount.items(), key=lambda x : x[1], reverse=True))

        ans = []
        for key, value in sorted_D.items():
            if value > (n / 3):
                ans.append(key)

        return ans
