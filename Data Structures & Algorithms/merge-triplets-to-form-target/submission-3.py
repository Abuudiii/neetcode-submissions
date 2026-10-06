class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = []

        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue

            valid.append([x, y, z])

        if valid:
            res = valid[0]
        else:
            return False
        
        for r in range(1, len(valid)):
            curr = valid[r]

            if curr == target:
                return True

            res = [max(curr[0], res[0]), max(curr[1], res[1]), max(curr[2], res[2])]

        return True if res == target else False

            