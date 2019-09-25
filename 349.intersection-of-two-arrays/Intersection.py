'''
Given two arrays, write a function to compute their intersection.
给定两个数组，编写一个函数来计算它们的交集
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

思路： 字典
'''

class Solution:
    def intersection(self,nums1, nums2):
        maps = {}
        result = []
        for num1 in nums1:
            maps[num1] = num1
        for num2 in nums2:
            if num2 in maps:
                result.append(num2)
                maps.pop(num2)
        return result

if __name__=="__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    s = Solution()
    result = s.intersection(nums1,nums2)
    for num in result:
        print (num)