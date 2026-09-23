class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prevTemp, prevIndex = stack.pop()
                res[prevIndex] = i - prevIndex

            stack.append([temp, i])
        
        return res