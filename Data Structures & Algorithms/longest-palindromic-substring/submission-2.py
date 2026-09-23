'''
- if we treat each element at s[i] as a center element
- we can keep track of longest palindrome by expanding outwards
- if neighbours are not equal then we can simply continue
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

            # even length
            l = i
            r = i + 1
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

        return res

