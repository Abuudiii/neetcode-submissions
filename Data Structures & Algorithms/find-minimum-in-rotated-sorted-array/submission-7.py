class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            - start l, m, r pointers
            - track current min from those
            - binary search on smaller window
        '''

        currMin = math.inf
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if l == r:
                return nums[l]

            if nums[l] < nums[r]:
                return nums[l]

            elif nums[m] > nums[r]:
                l = m + 1
            
            elif nums[m] <= nums[r]:
                r = m

        return nums[m]

            