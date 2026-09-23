class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        freqBucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        for num, cnt in numCount.items():
            freqBucket[cnt].append(num)

        res = []

        for i in range(len(freqBucket) - 1, 0, -1):
            for num in freqBucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
