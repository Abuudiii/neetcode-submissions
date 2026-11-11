class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)

        for num in seen:
            length = 1
            while num - 1 not in seen and num + length in seen:
                length += 1

            longest = max(longest, length)

        return longest