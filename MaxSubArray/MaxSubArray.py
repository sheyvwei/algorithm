'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
给定整数数组nums，找到具有最大总和并返回其总和的连续子数组（包含至少一个数字）
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
思路：动态规划,默认最大值和目前最大值为nums[0]， 遍历nums,通过一步步加nums[i]，判断目前最大的是数是相加的数，还是 仅仅是nums[i]，
最后通过判断目前最大值和记录的最大值哪个最大。遍历完nums，返回最大值
'''

class Solution:
    def maxSubArray(self,nums):
        maxCount = nums[0]
        currentCount = nums[0]
        for i in range(1, len(nums)):
            currentCount = max(currentCount+ nums[i], nums[i])
            maxCount = max(currentCount, maxCount)
        return maxCount



if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    result = s.maxSubArray(nums)
    print (result)