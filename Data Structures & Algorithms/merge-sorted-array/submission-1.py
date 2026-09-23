class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        '''
        - start writer from end of nums1
        - start leftReader from nums1 last valid element
        - start rightReader from nums2 last valid element
        - write 
        '''

        r1 = m - 1
        r2 = n - 1

        for i in reversed(range(len(nums1))):
            if r1 >= 0 and r2 >= 0:
                if nums1[r1] > nums2[r2]:
                    nums1[i] = nums1[r1]
                    r1 -= 1

                else:
                    nums1[i] = nums2[r2]
                    r2 -= 1

            elif r1 >= 0:
                nums1[i] = nums1[r1]
                r1 -= 1
            else:
                nums1[i] = nums2[r2]
                r2 -= 1


        return
        