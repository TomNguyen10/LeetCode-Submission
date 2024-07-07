class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0

        while numBottles >= numExchange:
            whole = numBottles // numExchange
            res += numExchange * whole
            numBottles -= numExchange * whole
            numBottles += whole
        
        return res + numBottles
