'''

Given a non-empty array of integers, every element appears twice except for one. Find that single one.
给定一个非空的整数数组，除了一个元素外，每个元素都会出现两次。找一个单一的
Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

思路： 异或操作，相同为0不同为1
'''

class Solution:
    def singleNumber(self,nums):
        start = 0
        for i in range(0,len(nums)):
            start ^= nums[i]
        return start


if __name__=="__main__":
    s = Solution()
    nums = [2,2,1]
    result = s.singleNumber(nums)
    print (result)