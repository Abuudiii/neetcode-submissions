class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans = 1
        seen = set()

        for num in nums:
            seen.add(num)

        for num in seen:
            if num - 1 not in seen:
                length = 1

                while (length + num) in seen:
                    length += 1

                ans = max(ans, length)

            
        return ans

        

        