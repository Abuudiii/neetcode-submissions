class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            a = numbers[l]
            b = numbers[r]
            if((a+b)>target):
                r-=1
            elif((a+b)<target):
                l+=1
            else:
                return [l+1,r+1]   
        return [l+1,r+1]    