'''

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
你是一个专业的强盗，计划在街上抢劫房屋。每个房子都有一定数量的钱存在，阻止你抢劫他们的唯一限制是相邻的房屋有连接的安全系统，
如果两个相邻的房子在同一个晚上被打破，它将自动联系警察。 给出一个代表每个房子的金额的非负整数列表，确定今晚可以抢劫的最大金额而不警告警察
Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

https://github.com/azl397985856/leetcode/blob/master/problems/198.house-robber.md
    思路： 动态规划问题，可以把O(n)的时间复杂度转化为 O(1)
        找到动态规划方程 dp[i] = max( dp[i-1], dp[i]+ dp[i-2])
        2. python交换两个数字  a,b = b, a
'''

class Solution:
    def houseRobber(self,nums):
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        else:
            pre = nums[0]
            cur = max(pre, nums[1])
            for i in range(2,length):
                temp = cur
                cur = max(pre + nums[i], cur)
                pre = temp

            return cur

    def houseRobber2(self,nums):
        #默认dp[0] = dp[1] = 0
        dp = [0 for x in range(0,1000)]
        dp[0] = 0
        dp[1] = 0
        length = len(nums)
        for i in range(2, length+ 2):
            dp[i] = max(dp[i-2] + nums[i-2], dp[i-1])
        return dp[length+1]

if __name__=="__main__":
    s = Solution()
    nums = [2,7,9,3,1]
    result = s.houseRobber(nums)
    print (result)

    nums = [1,2,3,1]
    result = s.houseRobber2(nums)
    print (result)

    nums = []
    result = s.houseRobber(nums)
    print (result)