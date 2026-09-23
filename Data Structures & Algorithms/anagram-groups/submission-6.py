class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            charCount = [0] * 26

            for char in word:
                charCount[ord(char) - ord('a')] += 1

            anagrams[tuple(charCount)].append(word)

        return list(anagrams.values())