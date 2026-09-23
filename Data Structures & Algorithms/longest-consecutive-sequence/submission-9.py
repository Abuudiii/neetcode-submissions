class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for num in nums:
            curr = 1
            while num - 1 not in seen and num + curr in seen:
                curr += 1

            res = max(res, curr)


        return res

        