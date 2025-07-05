class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = twenty = 0
        for i in bills:
            if i == 5:
                five +=1
            elif i == 10:
                if five:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif i == 20:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True