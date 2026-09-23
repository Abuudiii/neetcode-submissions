class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxLength = 1
        seen = set()

        for num in nums:
            seen.add(num)

        for num in seen:
            if num - 1 not in seen:
                length = 1
                while (length + num) in seen:
                    length += 1

                maxLength = max(length, maxLength)

        return maxLength


        

        