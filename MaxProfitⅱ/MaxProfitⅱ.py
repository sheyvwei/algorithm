'''
122 题
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
假设您有一个数组，其中第i个元素是第i天给定股票的价格。
设计算法以找到最大利润。
您可以根据需要完成尽可能多的交易（即，多次买入并卖出一股股票）。
 注意：您不得同时进行多笔交易（即，您必须在再次购买之前卖出股票）
Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

思路：只要把 与前一个数值有增长的向加就可以了
'''

class Solution:
    def maxProfit(self,prices):
        # if prices is None:
        #     return 0
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit



if __name__=='__main__':
    s = Solution()
    prices = [7,1,5,3,6,4]
    result = s.maxProfit(prices)
    print (result)










