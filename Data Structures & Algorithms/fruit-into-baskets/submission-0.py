'''
    - loop over the array until we can pick exactly 2 types of fruit
    - once a third type of fruit is encountered, store max, and shrink window from left until we have 2 types again
    - repeat until the end
'''

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        numFruits = 0
        fruitMap = {}
        l = 0

        for r in range(len(fruits)):
            while len(fruitMap) > 2:
                fruitMap[fruits[l]] -= 1

                if fruitMap[fruits[l]] == 0:
                    del fruitMap[fruits[l]]

                l += 1
            
            fruitMap[fruits[r]] = 1 + fruitMap.get(fruits[r], 0)

            if len(fruitMap) <= 2:
                numFruits = max(numFruits, sum(fruitMap.values()))

        return numFruits

                