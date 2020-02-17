class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profit,min_elem=0,prices[0]
        tp=0
        for i in range(1,len(prices)):
            min_elem=min(prices[i],min_elem)
            profit=prices[i]-min_elem
            if max_profit<profit:
                tp+=profit
                min_elem=prices[i]
                max_profit=0
        return tp
