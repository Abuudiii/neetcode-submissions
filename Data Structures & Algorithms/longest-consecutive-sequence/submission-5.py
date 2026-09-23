class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set()
        ans = 1

        for num in nums:
            numSet.add(num)

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                ans = max(ans, length)


        return ans



        

        