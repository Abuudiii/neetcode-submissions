class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        mappings = Counter(nums)

        for char, count in mappings.items():
            freq[count].append(char)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res
