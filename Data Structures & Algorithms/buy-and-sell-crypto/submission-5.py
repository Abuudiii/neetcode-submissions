class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        currMax = 0

        for r in range(1, len(prices)):
            total = prices[r] - prices[l]

            if total <= 0:
                l = r
            else:
                currMax = max(currMax, total)

        return currMax