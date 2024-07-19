class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # profit is zero
        # current_minimum is first value
        # for each value in the array
            # if value less than current minimum,
                # reset current minimum
            # set profit to different between value and current minimum
            # if greater than current profit

        profit = 0
        minimum = prices[0]

        for price in prices:
            minimum = min(minimum, price)
            profit = max(profit, price - minimum)

        return profit