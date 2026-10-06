class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
            - do merge sort
            - break into left and right subarrays
            - for each half, have a helper function sort it
        '''
        l, r = 0, len(nums) - 1

        def merge(array, l, m, r):
            left = array[l:m + 1]
            right = array[m + 1:r + 1]
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[l] = left[i]
                    i += 1

                else:
                    array[l] = right[j]
                    j += 1

                l += 1

            while i < len(left):
                array[l] = left[i]
                l += 1
                i += 1

            while j < len(right):
                array[l] = right[j]
                l += 1
                j += 1

        def mergeSort(arr, l, r):
            if l >= r:
                return

            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

        mergeSort(nums, l, r)
        return nums


        