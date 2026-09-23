class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numHeap = []
        heapq.heapify(numHeap)

        for num in nums:
            heapq.heappush(numHeap, num)

            if len(numHeap) > k:
                heapq.heappop(numHeap)

        return numHeap[0]