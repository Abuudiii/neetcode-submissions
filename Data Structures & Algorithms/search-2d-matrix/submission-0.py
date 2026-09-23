class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if matrix[m][0] > target:
                if target in matrix[m]:
                    return True
                r = m - 1
            elif matrix[m][0] < target:
                if target in matrix[m]:
                    return True
                l = m + 1
            else:
                return True

        return False
