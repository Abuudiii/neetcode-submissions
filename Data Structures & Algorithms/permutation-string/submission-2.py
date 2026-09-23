class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # slide a window of len(s1) over s2
        # helper function to see if permutation exists
        l = 0
        s1Map = {}
        s2Map = {}
        n = len(s1) - 1

        for c in s1:
            s1Map[c] = 1 + s1Map.get(c, 0)

        for r in range(len(s2)):
            s2Map[s2[r]] = 1 + s2Map.get(s2[r], 0)

            if r - l > n:
                s2Map[s2[l]] -= 1

                if s2Map[s2[l]] == 0:
                    del s2Map[s2[l]]
                l += 1

            
            print(s2Map)

            if s2Map == s1Map:
                return True

        return False

