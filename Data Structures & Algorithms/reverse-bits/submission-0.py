class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0

        for i in range(32):
            res = (1 << i) & n
            if res:
                rev += (1 << (31 - i))

        return rev
            