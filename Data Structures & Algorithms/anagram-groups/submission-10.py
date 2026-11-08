class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            mapping = [0] * 26

            for char in word:
                mapping[ord(char) - ord('a')] += 1

            res[tuple(mapping)].append(word)

        return list(res.values())