class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {}

        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        max_pair = max(numCount.items(), key=lambda x: x[1])

        return max_pair[0]