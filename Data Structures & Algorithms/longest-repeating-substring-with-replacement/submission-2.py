class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        wordMap = {}
        l = 0
        length = 0

        for r in range(len(s)):
            wordMap[s[r]] = 1 + wordMap.get(s[r], 0)

            while r - l + 1 - max(wordMap.values()) > k:
                wordMap[s[l]] -= 1
                l += 1

            length = max(length, r - l + 1)

        return length