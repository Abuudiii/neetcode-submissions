class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minHeap = []
        heapq.heapify(minHeap)
        tasks = sorted((eTime, pTime, idx) for idx, (eTime, pTime) in enumerate(tasks))
        res = []
        time, i = 0, 0

        while i < len(tasks) or minHeap:
            while i < len(tasks) and tasks[i][0] <= time:
                eTime, pTime, idx = tasks[i]
                heapq.heappush(minHeap, (pTime, idx))
                i += 1

            if minHeap:
                pTime, idx = heapq.heappop(minHeap)
                res.append(idx)
                time += pTime
            else:
                time = tasks[i][0]

        return res