class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prevIdx, prevTemp = stack.pop()
                res[prevIdx] = idx - prevIdx

            stack.append((idx, temp))

        return res