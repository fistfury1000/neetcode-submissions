class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for x in range(len(prices)):
            buy = prices[x]
            for j in range(x+1,len(prices)):
                sell = prices[j]
                profit = max(sell-buy,profit)
        return profit

