class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        mp = 0
        
        for i in prices:
            if i < minprice:
                minprice=i
            else :
                profit = i - minprice
                mp = max(mp, profit)
        return mp

          