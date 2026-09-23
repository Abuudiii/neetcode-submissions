'''
    - build out adj list based on words possible patterns
    - add the first first word to queue, and then loop over each layer
    - compute all possible patterns and do bfs on them
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]

                    for neighbour in nei[pattern]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour) 

            res += 1

        return 0