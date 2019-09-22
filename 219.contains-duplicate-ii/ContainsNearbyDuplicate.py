'''
219 https://leetcode.com/problems/contains-duplicate-ii/description/
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

思路： 字典存储 nums和 i
'''


class Solution:
    def containsNearbyDuplicate(self, nums, k):
         maps = {}
         for i in range(len(nums)):
             if nums[i] not in maps.keys():
                 maps[nums[i]] = i
             else:
                 print (abs(i - maps[nums[i]]))
                 if abs(i - maps[nums[i]]) <= k:
                     return True
                 else:
                     maps[nums[i]] = i
         return False

    def containsNearbyDuplicate2(self, nums, k):
        d = {}
        for index, num in enumerate(nums):
            if num in d and index - d[num] <= k:
                return True
            d[num] = index
        return False



if __name__=="__main__":
    nums = [1,0,1,1]
    k = 1
    s = Solution()
    result = s.containsNearbyDuplicate2(nums, k)
    print (result)
