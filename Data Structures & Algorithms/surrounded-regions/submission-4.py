class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(board), len(board[0])

        def dfs(r, c):
            if min(r, c) < 0 or r == ROW or c == COL or board[r][c] != "O":
                return

            board[r][c] = "#"

            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        for r in range(ROW):
            dfs(r, 0)
            dfs(r, COL - 1)

        for c in range(COL):
            dfs(0, c)
            dfs(ROW - 1, c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

        