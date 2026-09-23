class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [x for x in stones]
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            x, y = heapq.heappop_max(maxHeap), heapq.heappop_max(maxHeap)

            if x > y:
                heapq.heappush_max(maxHeap, x - y)

        maxHeap.append(0)
        return maxHeap[0]