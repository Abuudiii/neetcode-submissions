class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        skipFirst = nums[1:]
        skipSecond = nums[:n]

        return max(nums[0], self.robHouses(skipFirst), self.robHouses(skipSecond))
        

    def robHouses(self, houses):
        rob1, rob2 = 0, 0

        for num in houses:
            tmp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2