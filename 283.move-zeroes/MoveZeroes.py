'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
给定一个数组num，编写一个函数，将所有0移到它的末尾，同时保持非零元素的相对顺序。不能复制数组
Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
思路： 头尾双指针(不能保持非零元素的相对位置） 错误
        快慢指针，可以保持相对位置
'''

class Solution:
    def moveZeroes(self, nums):
        slow = fast = 0
        while fast< len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums

    def moveZeroes2(self,nums):
        left = 0
        right = len(nums) - 1
        for i in range(len(nums)):
            if nums[right] == 0 and i < right:
                right -= 1
                continue
            if nums[i] == 0 and i < right:
                nums[i], nums[right] = nums[right], nums[i]
                continue
        return nums

if __name__=="__main__":
    s = Solution()
    nums = [0,1,0,3,12]
    result = s.moveZeroes(nums)
    # result = s.moveZeroes2(nums)
    for num in nums:
        print (num)

