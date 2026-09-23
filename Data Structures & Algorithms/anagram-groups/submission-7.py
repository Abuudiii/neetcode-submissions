class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            fingerPrint = [0] * 26

            for char in word:
                fingerPrint[ord(char) - ord("a")] += 1

            res[tuple(fingerPrint)].append(word)

        return list(res.values())

