class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ''' 
            - keep a window with frequency of each char
            - check if the freq of the most common char - legnth of window is within k replacements
            - if it is not, shrink from left until it is, elif take the max of curr window and prev window
        '''
        length = 0
        l = 0
        currMap = {}

        for r in range(len(s)):
            currMap[s[r]] = 1 + currMap.get(s[r], 0)
            
            while r - l + 1 - max(currMap.values()) > k:
                currMap[s[l]] -= 1

                if currMap[s[l]] == 0:
                    del currMap[s[l]]
        
                l += 1

            length = max(length, r - l + 1)

        return length