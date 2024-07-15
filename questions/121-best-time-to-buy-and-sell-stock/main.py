from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # naive way - check all buy-sell pairs and find the maximum profit
        # - O(n^2) time complexity
        # - O(1) memory, just a couple of variables to store the max profit

        # better way: 
        # - find the buy-sell window that yields the largest profit
        # - if no profits possible, return 0
        # - "buy" must occur before "sell", hence a window
        # - no restrictions on window size (ie. no fixed timeframe between which we must buy/sell)

        if len(prices) < 2: return 0 # buy + sell on same day yields no profit

        l, r = 0, 1
        profit = 0

        while r < len(prices):
            buy, sell = prices[l], prices[r]
            if buy > sell:
                # yields negative profit, try buying at the lower price instead
                l = r
            else:
                # buy <= sell, may yield a profit.
                profit = max(profit, sell - buy)        
            # expand window to check other buy-sell pairs
            r += 1
        
        return profit