class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0

        for i in range(len(prices)):

            if i + 1 < len(prices):
                margin = prices[i + 1] - prices[i]

                if margin <= 0:
                    continue

                maxProf += margin
                
        return maxProf

            