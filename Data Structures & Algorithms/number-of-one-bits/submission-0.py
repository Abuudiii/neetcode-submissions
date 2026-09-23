class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            bit = (1 << i) & n
            if bit:
                count += 1

        return count

