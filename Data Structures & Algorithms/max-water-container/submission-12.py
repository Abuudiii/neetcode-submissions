class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        l, r = 0, len(heights) - 1

        while l < r:
            minHeight = min(heights[l], heights[r])
            maxAmount = max(maxAmount, minHeight * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxAmount