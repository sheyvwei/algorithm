'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。\

思路： 最大利润便是 波峰 与 波谷的 差值
        计算差值，  for循环中 先比较 nums[i]是否比  上一个波谷的值 小， 如果是，它就是波谷，
        然后计算 nums[i]与波谷的差值，如果它比最大利润 max_profit大，那么它就是最大利润
'''



class Solution:
    def maxProfit(self,prices):
        if prices is None:
            return 0
        # python申明正负无穷大
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif max_profit < price - min_price:
                max_profit = price - min_price
        return max_profit
    #嵌套for，不建议
    def maxProfitByMySelf(self,nums):
        length = len(nums)
        count = 0
        for i in range(0,length-1):
            for j in range(i,length-1):
                a = nums[j]
                b = nums[i]
                count = max(count, nums[j]-nums[i])

        return count


if __name__=="__main__":
    s = Solution()
    nums = [7,1,5,3,6,4]
    result = s.maxProfit(nums)
    print (result)








