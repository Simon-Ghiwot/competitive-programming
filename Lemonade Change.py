class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10 and fives == 0:
                return False
            elif bill == 10:
                fives -= 1
                tens += 1
            elif bill == 20:
                total = fives * 5 + tens * 10
                if total < 15 or fives == 0:
                    return False
                else:
                    tens -= 1
                    fives -= 1
        return True

                
