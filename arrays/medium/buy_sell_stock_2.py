"""
Author: amisha26
Question Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                s += (prices[i] - prices[i - 1])
        
        return s