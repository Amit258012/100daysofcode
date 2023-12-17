# https://leetcode.com/problems/online-stock-span/
"""
Time complexity:- O(N)
Space Complexity:- O(N)
"""

"""
Intuition:

The StockSpanner class maintains a monotonic stack (monotone_stack) to store stock entry information.
A stock entry consists of two parameters: price_quote (the current stock price) and price_span (the span of stock prices).
The next method is called to process the next stock price and calculate its span.
"""


class StockSpanner:
    def __init__(self):
        # Maintain a monotonic stack for stock entry

        ## Definition of stock entry:
        # First parameter is price quote
        # Second parameter is price span
        self.monotone_stack = []

    def next(self, price: int) -> int:
        stack = self.monotone_stack

        cur_price_quote, cur_price_span = price, 1

        # Compute price span in stock data with monotonic stack
        while stack and stack[-1][0] <= cur_price_quote:
            prev_price_quote, prev_price_span = stack.pop()

            # Update current price span with history data in stack
            cur_price_span += prev_price_span

        # Update latest price quote and price span
        stack.append((cur_price_quote, cur_price_span))

        return cur_price_span
