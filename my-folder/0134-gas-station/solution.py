class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas, currentGas = 0, 0
        start = 0
        for i in range(len(gas)):
            totalGas += gas[i] - cost[i]
            currentGas += gas[i] - cost[i]
            if currentGas < 0:
                start = i + 1
                currentGas = 0
        if totalGas < 0:
            return -1
        return start
        
