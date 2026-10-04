class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for w in strs:
            mapping = [0] * 26

            for c in w:
                mapping[ord(c) - ord('a')] += 1

            anagrams[tuple(mapping)].append(w)

        return list(anagrams.values())