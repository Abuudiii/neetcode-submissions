class Solution:
    def minWindow(self, s: str, t: str) -> str:


        def isValidWindow(tMap, windowMap):
            for char, count in tMap.items():
                if windowMap.get(char, 0) < count:
                    return False

            return True
        
        l = 0 
        r = 0
        currMin = len(s)
        res = ""
        tMap = {}
        windowMap = {}

        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)

        for r in range(len(s)):
            windowMap[s[r]] = 1 + windowMap.get(s[r], 0)

            while isValidWindow(tMap, windowMap):
                if (r - l + 1) <= currMin:
                    currMin = r - l + 1
                    res = s[l:r+1]
                
                windowMap[s[l]] -= 1
                l += 1

        return res

            
