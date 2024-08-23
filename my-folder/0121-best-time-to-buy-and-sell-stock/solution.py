class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPurchase = prices[0]

        for i in range(1, len(prices)):
            res = max(res, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        
        return res
