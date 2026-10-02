class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1
                continue

            elif bill == 10:
                if fives < 1:
                    return False

                fives -= 1
                tens += 1
            
            elif bill == 20:
                if tens >= 1 and fives >= 1:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False

        return True


                


             