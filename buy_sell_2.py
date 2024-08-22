class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy=float('inf')
        max_profit=0
        for i in prices:
            if buy>i:
                buy=i
            elif buy<i:
                max_profit+=(i-buy)
                buy=i
        return max_profit
prices=[7,1,5,3,6,4]
obj=Solution()
profit=obj.maxProfit(prices)
print(profit)
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.