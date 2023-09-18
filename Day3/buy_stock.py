"""
        Find the maximum profit that can be obtained from buying and selling a single stock.

        Args:
            prices (List[int]): A list of stock prices.

        Returns:
            int: The maximum profit.
"""


class Solution:
    def maxProfit(self, prices):
        max_profit = 0  # Initialize the maximum profit to 0.
        buy_price = prices[0]  # Initialize the buy price with the first stock price.

        for price in prices:
            if price < buy_price:
                # If the current price is lower than the buy price, update the buy price.
                buy_price = price
            else:
                # If the current price is higher, calculate the profit and update max_profit if needed.
                max_profit = max(max_profit, price - buy_price)

        return max_profit
