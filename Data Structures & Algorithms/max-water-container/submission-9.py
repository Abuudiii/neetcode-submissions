class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            minHeight = min(heights[l], heights[r])
            dist = r - l
            area = max(area, minHeight * dist)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return area
