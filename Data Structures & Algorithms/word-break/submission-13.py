class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dfs(word):
            if word == s:
                return True
            
            if len(word) > len(s):
                return False

            if word in cache:
                return cache[word]

            can = False
            for i in range(len(wordDict)):
                if s[len(word):].startswith(wordDict[i]):
                    new = word + wordDict[i]
                    can = can or dfs(new)


            cache[word] = can
            return cache[word]

        return dfs("")