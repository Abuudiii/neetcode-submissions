
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
            - visited set
            - adj list
            - deque
        '''
        visited = set()
        adj = defaultdict(list)
        minHeap = []
        heapq.heapify(minHeap)
        time = 0

        for src, dst, cost in times:
            adj[src].append([dst, cost])

        heapq.heappush(minHeap, (0, k))

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            
            if node in visited:
                continue

            time = cost
            visited.add(node)

            for neighbor, n_cost in adj[node]:
                heapq.heappush(minHeap, [cost + n_cost, neighbor])

        if len(visited) != n:
            return -1

        return time