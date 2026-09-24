class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
            - iterate over a window of size k over the array
            - at each new elem, expand the window
            - if window is greater than k, check if the curr elem is closer
            - if so shrink window from left
        '''

        l = 0
        start, end = 0, 0

        for i in range(len(arr)):
            r = i
            if r - l + 1 > k:
                right = arr[r] - x
                left = x - arr[l]

                if right < left:
                    l += 1
                    start = l
                elif right >= left:
                    break

            end = r

        return arr[start:end+1]
                
                    
