class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            - create mapping of s1
            - go over a window of s1 range in s2
            - return True if it matches, else False if not found
        '''
        mapping = Counter(s1)
        pMapping = {}
        l = 0

        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                pMapping[s2[l]] -= 1
                if pMapping[s2[l]] == 0:
                    del pMapping[s2[l]]
                
                l += 1
            
            pMapping[s2[r]] = 1 + pMapping.get(s2[r], 0)

            if pMapping == mapping:
                return True


        return False
