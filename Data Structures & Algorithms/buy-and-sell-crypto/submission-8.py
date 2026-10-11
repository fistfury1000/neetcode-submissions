class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lebron = 0
        for x in range(len(prices)):
            poop= prices[x]
            for j in range(x+1, len(prices)):
                kaka = prices[j]
                lebron = max(lebron,kaka-poop)
        return lebron
        