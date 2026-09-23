class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            distance = r - l
            minHeight = min(heights[l], heights[r])
            currMax = max(currMax, minHeight * distance)

            if heights[l] < heights[r]:
                l += 1
                continue

            elif heights[l] > heights[r]:
                r -= 1
                continue
            
            r -= 1

        
        return currMax

