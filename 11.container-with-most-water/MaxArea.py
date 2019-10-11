'''

11.盛最多水的容器
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

Note: You may not slant the container and n is at least 2.
思路： 双指针， 移动最小的值，便可计算出最大面积
5.
https://segmentfault.com/a/1190000020107909?utm_source=tag-newest
'''

class Solution:
    def maxArea(self, s):
        left = 0
        right = len(s) -1
        maxArea = 0
        for i in range(len(s)-1):
            maxArea = max(maxArea, min(s[left] , s[right]) * (right - left))
            if s[left] > s[right]:
                right -= 1
            else:
                left += 1
        return maxArea


if __name__=="__main__":
    s = Solution()
    nums = [1,8,6,2,5,4,8,3,7]
    nums= [2,3]
    maxArea = s.maxArea(nums)
    print (maxArea)
