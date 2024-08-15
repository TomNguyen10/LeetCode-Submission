class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet = [0] * 3

        for bill in bills:
            if bill == 5:
                wallet[0] += 1
            if bill == 10:
                if wallet[0] == 0:
                    return False
                wallet[0] -= 1
                wallet[1] += 1
            elif bill == 20:
                if wallet[1] >= 1 and wallet[0] >= 1:
                    wallet[1] -= 1
                    wallet[0] -= 1
                elif wallet[0] >= 3:
                    wallet[0] -= 3
                else:
                    return False
                wallet[2] += 1
        
        return True
