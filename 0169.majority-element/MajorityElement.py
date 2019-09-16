'''
169. https://leetcode.com/problems/majority-element/description/
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
给定大小为n的数组，找到多数元素。多数元素是出现超过n /⌋倍的元素。
您可以假设该数组非空，并且多数元素始终存在于数组中
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

思路： 投票算法：节省空间复杂度。   n/2 
    多数元素大于 n/2 ，虽然可以直接 一个 n循环，记录 每个元素的数量，但是会带来 多余的空间，可以用投票算法，节省多余空间

'''


class Solution:
    def majorityElement(self,nums):
        count, majority = 1, nums[0]
        for num in nums[1:]:
            if count == 0:
                #当元素不是多数元素的时候，它数量会变0，此时要跟换元素
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1
        return majority
    def majorityElement2(self,nums):
        map = {}

        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1

            if map[nums[i]] > len(nums) / 2:
                return nums[i]

if __name__=="__main__":
    nums = [2,2,1,1,1,2,2]
    s = Solution()
    result = s.majorityElement(nums)
    print (result)
    ## 76   36
    nums = [3,2,3]
    r = s.majorityElement2(nums)
    print (r)
