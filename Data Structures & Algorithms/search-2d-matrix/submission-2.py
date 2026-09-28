class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
            - use first and last element to determine if we need to a do a bs in this array
            - if target greater than last element, move to next array
            - otherwise move to previous array
        '''

        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            
            if target > matrix[m][-1]:
                l = m + 1

            elif target < matrix[m][0]:
                r = m - 1

            else:
                inner = matrix[m]
                L, R = 0, len(inner) - 1

                while L <= R:
                    M = L + ((R - L) // 2)

                    if target > inner[M]:
                        L = M + 1
                    elif target < inner[M]:
                        R = M - 1
                    elif inner[M] == target:
                        return True

                return False

        return False