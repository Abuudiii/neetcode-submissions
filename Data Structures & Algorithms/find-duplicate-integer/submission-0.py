class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

        for key in seen:
            if seen[key] > 1:
                return key
