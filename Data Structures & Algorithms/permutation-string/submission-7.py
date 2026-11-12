class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapping = Counter(s1)
        wordMap = {}
        l = 0

        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                wordMap[s2[l]] -= 1

                if wordMap[s2[l]] == 0:
                    del wordMap[s2[l]]

                l += 1

            wordMap[s2[r]] = 1 + wordMap.get(s2[r], 0)

            if wordMap == mapping:
                return True

        return False
