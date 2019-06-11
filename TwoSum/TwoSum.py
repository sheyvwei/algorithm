
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
思路：遍历每个数组，与目标的差值作为字典的key，哪个位置作为 value（后面需要返回位置），
如果这个差值不存在这个字典中，则放入字典，
如果存在，则直接通过字典[key]得到目标位置及该元素位置i 返回
o(n)时间换空间sss
'''

class Solution:
    def TwoSum(nums, target):
        """
        :type nums: List[int]
        :type target:int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict.keys():
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]], i]

if __name__ == '__main__':

    nums = [2, 7, 11,15]
    target = 9
    print(Solution.TwoSum(nums,target))


