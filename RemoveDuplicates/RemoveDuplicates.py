'''
题目 26：
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
给定排序的数组nums，就地删除重复项，使每个元素只出现一次并返回新的长度
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
不要为另一个数组分配额外的空间，必须通过使用O（1）额外内存修改输入数组来实现此目的

思路： 快慢指针
Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length. Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
        if nums:
            slow = 0
            for fast in range(1,len(nums)):
                if nums[slow] !=nums[fast]:
                    slow += 1
                    nums[slow] = nums[fast]
            return slow +1
        else:
            return 0
'''

class Solution:
    def RemoveDuplicates(self,nums):
        if nums:
            slow = 0
            for fast in range(1, len(nums)):
                if nums[slow] != nums[fast]:
                    slow += 1
                    nums[slow] = nums[fast]
            return slow + 1
        else:
            return 0

if __name__ == '__main__':
    s = [1,1,2]
    solution = Solution()
    result = solution.RemoveDuplicates(s)
    print (result)
