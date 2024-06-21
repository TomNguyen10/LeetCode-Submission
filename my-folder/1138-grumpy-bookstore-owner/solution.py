class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        fixed = 0
        res = 0
        curr = 0

        for i in range(len(grumpy)):
            sas = grumpy[i]
            cus = customers[i]

            if sas == 0:
                fixed += cus
                customers[i] = 0
            
            curr += customers[i]

            if i >= minutes:
                curr -= customers[i - minutes]
            
            res = max(res, curr)
        
        return res + fixed

