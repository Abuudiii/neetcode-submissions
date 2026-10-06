class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
            - start at 0, 0
            - calculate each neighbours effort
            - track the max effort and push it to the minHeap
            - we take the smallest max effort to get to r, c
            - tracking it means at r, c we already have the answer
        '''
        ROW, COL = len(heights), len(heights[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        minHeap = []
        heapq.heapify(minHeap)

        # 1. while q is valid (not at r, c), pop the top element in the heap and do bfs on it
        def bfs(r, c, prev, effort):
            if min(r, c) < 0 or r == ROW or c == COL or (r, c) in visited:
                return

            effort = max(effort, abs(heights[r][c] - prev))
            heapq.heappush(minHeap, (effort, r, c))

        heapq.heappush(minHeap, (0, 0, 0))

        # 2. keep going untl r, c is reached
        while minHeap:
            e, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            if r == ROW - 1 and c == COL - 1:
                return e

            visited.add((r, c))

            for dr, dc in dirs:
                bfs(r + dr, c + dc, heights[r][c], e)