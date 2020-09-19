class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxprice = 0
        minprice = float("inf")
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1] :
                minprice = min(minprice,prices[i])
                maxprice= max(maxprice,prices[i+1] -minprice)
                
        return maxprice
