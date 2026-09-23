class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
            - maintain a sliding window of size k and see if a duplicate exists in that window
        '''

        l = 0
        seen = set()

        for r in range(len(nums)):
            if r - l > k:
                seen.remove(nums[l])
                l += 1

            if nums[r] in seen:
                return True

            seen.add(nums[r])

        return False