'''
    - dfs from edge 0s and mark them and their adjacent neighbours as #
    - rest remainig 0s are always surrounded so they can easily be converted
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(board), len(board[0])


        def dfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or board[r][c] == "X" or board[r][c] == "#":
                return

            board[r][c] = "#"

            for dr, dc in dirs:
                dfs(r + dr, c + dc)


        for r in range(ROW):
            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][COL - 1] == "O":
                dfs(r, COL - 1)

        for c in range(COL):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROW - 1][c] == "O":
                dfs(ROW - 1, c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"