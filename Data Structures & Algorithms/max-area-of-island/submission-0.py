'''
    - go over each element
    - once a '1' is found, dfs and keep track of area, and store it as a max

'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        q = deque()
        ROW, COLUMN = len(grid), len(grid[0])
        max_area = 0

        def bfs():
            area = 0
            while q:
                r, c = q.popleft()
                area += 1
                
                for dr, dc in dirs:
                    if min(r + dr, c + dc) < 0 or r + dr == ROW or c + dc == COLUMN or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == 0:
                        continue

                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))

            return area


        for r in range(ROW):
            for c in range(COLUMN):
                if (r, c) not in visited and grid[r][c] == 1:
                    q.append((r, c))
                    visited.add((r, c))
                    max_area = max(max_area, bfs())

        return max_area

                
                

