from typing import List


# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at
# any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.


class Solution:
    def getBuyDays(self, prices: List[int]) -> List[int]:
        res = []
        if len(prices) > 1 and prices[0] < prices[1]:
            res.append(0)

        for i in range(1, len(prices) - 1):
            yesterday_price = prices[i - 1]
            tomorrow_price = prices[i + 1]
            if prices[i] <= yesterday_price and prices[i] < tomorrow_price:
                res.append(i)

        return res

    def getSellDays(self, prices: List[int]) -> List[int]:
        res = []

        for i in range(1, len(prices) - 1):
            yesterday_price = prices[i - 1]
            tomorrow_price = prices[i + 1]
            if prices[i] > yesterday_price and prices[i] >= tomorrow_price:
                res.append(i)

        if prices[len(prices) - 1] > prices[len(prices) - 2]:
            res.append(len(prices) - 1)

        return res

    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        buy_days = self.getBuyDays(prices)
        sell_days = self.getSellDays(prices)

        for b, s in zip(buy_days, sell_days):
            res += prices[s] - prices[b]

        return res

    def maxProfitOptimized(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
    print(sol.maxProfitOptimized([7, 1, 5, 3, 6, 4]))
