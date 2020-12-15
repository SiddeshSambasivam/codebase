# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Trick: min cakue in the past should be used to maximize the profit using the present value at every iteration

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # base case
        if len(prices) == 0:
            return 0

        # 7,1,5,3,6,4
        # max sell - min cost  = max profit

        # remember the min past value and subtract that with the present to check if it maximises the profit
        min_ = prices[0]
        profit = 0
        for ele in prices[1:]:

            profit = max(0, profit, ele - min_)
            min_ = min(min_, ele)

        return profit

        # trial run
        # prices = [3, 2, 4, 1, 6, 7]
        # min = 3
        # 0: profit = 0
        #
        # 1: profit = 0 ; min = 2
        #
        # 2: profit = 4 - 2 = 2 ; min = 2
        #
        # 3: profit = 1 - 2 => 2 ; min = 1
        #
        # 4: profit = 6-1 = 5 ; min = 1
        #
        # 5: profit = 7 - 1 = 6 ; min =1
        #
        # resutl = 6
