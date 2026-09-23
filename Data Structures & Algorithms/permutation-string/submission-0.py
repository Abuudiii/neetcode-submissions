class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        l = 0
        chars = [0] * 26
        freq = [0] * 26

        for c in s1:
            chars[ord(c) - ord('a')] += 1
        
        for r in range(len(s2)):
            freq[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 > len(s1):
                freq[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if freq == chars:
                return True
            

        return False