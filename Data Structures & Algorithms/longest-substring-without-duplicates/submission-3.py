class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        visited = set()
        maxLength = 0

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1

            visited.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength