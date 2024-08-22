class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy,sell=float('inf'),0
        for i in range(len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            elif sell<(prices[i]-buy):
                sell=prices[i]-buy
        if sell==float('-inf'):
            sell=0
        return sell
prices=[7,1,5,3,6,4]
obj=Solution()
profit=obj.maxProfit(prices)
print(profit)
