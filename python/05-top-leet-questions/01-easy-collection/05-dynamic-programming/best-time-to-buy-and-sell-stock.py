
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
from typing import List


class Solution:
    # Two Pointer solution
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        res = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > 0:  # left is still minimum
                res = max(res, profit)
            else:
                left = right
            right += 1
        return res

    INT_MAX = 10 ** 4 + 1
    INT_MIN = -1

    def maxProfitAlt(self, prices: List[int]) -> int:
        buy, profit = self.INT_MAX, 0
        for p in prices:
            buy = min(buy, p)
            profit = max(profit, p-buy)
        return profit

    def maxProfitExtended(self, prices: List[int]) -> int:
        res = (-1, -1, 0)  # start, end, profit
        cand_min = (-1, self.INT_MAX)  # idx, price
        cand_max = (-1, self.INT_MIN)

        for i in range(len(prices)):
            p = prices[i]
            if p < cand_min[1]:
                cand_min = (i, p)
                cand_max = (-1, self.INT_MIN)  # reset
            elif p > cand_max[1]:
                cand_max = (i, p)
            cand_profit = cand_max[1] - cand_min[1]
            if cand_profit > res[2]:
                res = (cand_min[0], cand_max[0], cand_profit)
        return res[2]


if __name__ == "__main__":
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))
    print(sol.maxProfitAlt(prices))
    print(sol.maxProfitExtended(prices))
