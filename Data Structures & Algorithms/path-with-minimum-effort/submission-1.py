class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
            - keep visited set to avoid cycling
            - start with 0, 0
            - calc neighbour efforts and cords and push to minheap
            - make sure for each neighbour u calc its effort vs effort so far
            - this way dijkstra takes the smallest path naturally
            - at r, c answer bubbles down
        '''
        visited = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(heights), len(heights[0])
        minHeap = []
        heapq.heapify(minHeap)

        def bfs(r, c, effort, prev):
            if min(r, c) < 0 or r == ROW or c == COL or (r, c) in visited:
                return

            effort = max(effort, abs(heights[r][c] - prev))
            heapq.heappush(minHeap, (effort, r, c))
        
        heapq.heappush(minHeap, (0, 0, 0))

        while minHeap:
            effort, r, c = heapq.heappop(minHeap)
            
            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == ROW - 1 and c == COL - 1:
                return effort

            for dr, dc in dirs:
                bfs(r + dr, c + dc, effort, heights[r][c])


        