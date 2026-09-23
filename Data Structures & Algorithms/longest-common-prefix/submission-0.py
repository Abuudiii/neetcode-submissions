class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maximum = max(strs)
        minimum = min(strs)
        prefix = ""

        for i in range(len(minimum)):
            if maximum[i] == minimum[i]:
                prefix += maximum[i]
            else:
                break

        return prefix





