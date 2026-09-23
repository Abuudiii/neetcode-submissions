class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        '''
            - go through each num, track curr length
            - see if it can be the starting of a sequence
            - while curr length + 1 exists, continue looping
            - once false, store max of prev longest and curr length
            - continue until all inputs are processed
        '''

        for num in numSet:
            # starting of sequence
            if num - 1 not in numSet:
                curr = num
                currLength = 1

                while curr + 1 in numSet:
                    curr += 1
                    currLength += 1

                longest = max(longest, currLength)
                continue
            
        return longest
