class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [x for x in stones]
        heapq.heapify_max(stones)

        while len(stones) > 1:
            # grabbing two largest stones from heap
            first  = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            # pushing if stones differ in weight
            if first > second:
                heapq.heappush_max(stones, first - second)

        stones.append(0)
        return stones[0]