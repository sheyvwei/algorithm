'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
给定已按升序排序的整数数组，找到两个数字，
使它们相加到特定的目标数。 函数twoSum应返回两个数字的索引，
以便它们加起来到目标，其中index1必须小于index2。 注意： 您返回的答案（index1和index2）不是从零开始的

思路： 字典或者双指针

'''

class Solution:
    def twoSum(self, numbers, target):
        maps = {}
        for i in range(len(numbers)):
            if target - numbers[i] in maps.keys():
                return [maps[target-numbers[i]],i + 1]
            else:
                maps[numbers[i]] = i + 1


if __name__=="__main__":
    numbers = [2,7,11,15]
    target = 9
    s = Solution()
    result = s.twoSum(numbers,target)
    print (result)
