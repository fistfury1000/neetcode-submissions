class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        remainder = 0
        for x in range(0, len(prices)):
            buy = prices[x]
            for j in range(x+1, len(prices)):
                sell = prices[j]
                remainder= max(remainder, sell-buy)
        return remainder
        