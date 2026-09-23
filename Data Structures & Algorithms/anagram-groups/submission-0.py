class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            fingerPrint = [0] * 26

            for c in s:
                fingerPrint[ord(c) - ord("a")] += 1
            
            anagrams[tuple(fingerPrint)].append(s)

        return list(anagrams.values())