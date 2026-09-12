class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j]- prices[i]; #buyingPrice = price[i] , seelingPrice= price[j]
                maxProfit = max(profit, maxProfit)
        return maxProfit