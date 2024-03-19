#!/usr/bin/env python3

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            p_profit = price - min_price
            max_profit = max(max_profit, p_profit)
        return max_profit

# Test cases
if __name__ == "__main__":
    # Test case 1
    prices1 = [7,1,5,3,6,4]
    solution = Solution()
    print("Test case 1:", solution.maxProfit(prices1))  # Expected: 5

    # Test case 2
    prices2 = [7,6,4,3,1]
    print("Test case 2:", solution.maxProfit(prices2))  # Expected: 0