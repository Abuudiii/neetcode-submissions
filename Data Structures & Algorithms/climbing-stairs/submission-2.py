class Solution:
    def climbStairs(self, n: int) -> int:
        back, front = 1, 1

        for i in range(n):
            tmp = front
            front = front + back
            back = tmp
        
        return back