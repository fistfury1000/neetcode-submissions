class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        poop = 0
        for x in range(len(prices)):
            buy = prices[x]
            for j in range(x+1, len(prices)):
                sell = prices[j]
                poop = max(poop, sell-buy)
        return poop

        