class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROW, COLUMN = len(image), len(image[0])
        curr = image[sr][sc]

        if curr == color:
            return image

        def dfs(sr, sc, curr):
            if (min(sr, sc) < 0 or sr >= ROW or sc >= COLUMN or image[sr][sc] != curr):
                return

            image[sr][sc] = color

            for dr, dc in dirs:
                dfs(sr + dr, sc + dc, curr)

        dfs(sr, sc, curr)
        return image