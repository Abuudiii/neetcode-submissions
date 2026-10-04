class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        
        for num in nums:
            curr = 1

            while num - 1 not in seen and num + curr in seen:
                curr += 1

            longest = max(longest, curr)

        return longest