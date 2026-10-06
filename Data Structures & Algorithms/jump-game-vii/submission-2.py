class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            
            start = i + minJump
            if start <= farthest:
                start = farthest + 1

            end = min(i + maxJump, len(s) - 1)

            for j in range(start, end + 1):
                if s[j] == "0":
                    if j == len(s) - 1:
                        return True

                    q.append(j)

            farthest = end

        return False
