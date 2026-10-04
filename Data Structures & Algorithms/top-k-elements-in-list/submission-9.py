class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        counts = Counter(nums)

        for num, cnt in counts.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                if len(res) == k:
                    return res

                res.append(n)

        return res