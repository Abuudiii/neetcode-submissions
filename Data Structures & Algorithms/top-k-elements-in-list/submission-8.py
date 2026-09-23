class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for num, freq in freq.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for val in bucket[i]:
                res.append(val)

                if len(res) == k:
                    return res
                