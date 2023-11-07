class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            remainder = numBottles % numExchange
            numBottles = numBottles // numExchange
            res += numBottles
            numBottles += remainder
        return res
        
