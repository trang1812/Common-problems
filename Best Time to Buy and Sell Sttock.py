# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:45:39 2023

@author: Win 10
"""

'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

#Solution 1
class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        for i in range(len(prices)):
            profit = max(prices[(i):])-prices[i]
            if profit>max_profit:
                max_profit=profit
            else: pass
        return max_profit
    
#Solution 2
class Solution(object):
    def maxProfit(self, prices):
        max_profit=max(prices)-prices[0]
        for price in prices:
            index=prices.index(price)
            profit = max(prices[index:])-price
            if profit > max_profit:
                max_profit=profit
        return max_profit
    
#test
prices=[3,5,9,3,2,7]
Solution().maxProfit(prices)