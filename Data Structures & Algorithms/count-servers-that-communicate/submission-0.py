'''
    - loop over input
    - once we find a 1, check the entire row/column
    - if there is another 1 then the servers can communicate
'''

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        r_cnt = [0] * ROW
        c_cnt = [0] * COL
        res = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    r_cnt[r] += 1
                    c_cnt[c] += 1

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    continue

                if max(r_cnt[r], c_cnt[c]) > 1:
                    res += 1 

        return res
            


