class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                currSum = a + nums[l] + nums[r]

                if currSum < 0:
                    l += 1
                    continue
                elif currSum > 0:
                    r -= 1
                    continue
                else:
                    results.append([a, nums[l], nums[r]])
                    
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return results
                

                    

