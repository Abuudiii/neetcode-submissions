'''
    - keep a window that is the same length as the char
    - at each length, compare the hash sets of the current window with the s1 hash set
    - 
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        charSet = {}
        windowSet = {}

        # Build out the hash set of s1
        for char in s1:
            charSet[char] = 1 + charSet.get(char, 0)

        # Loop with window
        for r in range(len(s2)):
            windowSet[s2[r]] = 1 + windowSet.get(s2[r], 0)

            if r - l + 1 > len(s1):
                print(windowSet)
                windowSet[s2[l]] -= 1
                if windowSet[s2[l]] == 0:
                    del windowSet[s2[l]]

                l += 1


            if windowSet == charSet:
                return True

        return False

        

                