'''
[
    [1, 1, 0],
    [0, 1, 1],
    [0, 1, 2]
]

- track and fresh and rotten
- go through rotten
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        fresh = 0
        time = 0
        q = deque()
        ROW, COLUMN = len(grid), len(grid[0])

        for i in range(ROW):
            for j in range(COLUMN):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        while q and fresh:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in dirs:
                    row, col = r + dr, c + dc

                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
                
            time += 1

        return time if fresh == 0 else -1











