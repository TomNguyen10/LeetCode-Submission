class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, curr = 0, 0
        res = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]

            if curr < 0:
                res = i + 1
                curr = 0
        
        if total < 0:
            return - 1

        return res
