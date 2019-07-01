'''
https://www.jianshu.com/p/588caa7567c1
LeetCode 15:三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 *a，b，c ，*使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

思路：
    排序，然后循环取数a， 用双指针，left和right向中间取值，如果两个数的值为 nums[left] + nums[right] + a = 0则记录该数组
'''
class Solution:
    def threeSum(self, nums):
        '''
        :param nums: List[int]
        :return:    List[List[int]
        '''
        nums.sort()
        count = len(nums)
        collect = []
        for i in range(count):
            left = i + 1
            right = count - 1
            # 如果第一个数就大于0则返回
            if(nums[0] > 0):
                return collect
            #重复数字跳过
            if( i > 0 and nums[i] ==nums[i-1]):
                left += 1
                continue
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum == 0:
                    collect.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    print ( str(left) +'+'+  str(right))
                    ##排除重复项
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left +=1

        return collect

if __name__ ==  '__main__':
    nums = [-1,0,1,2,-1,-4]
    counts = len(nums)
    print (counts)
    s = Solution()
    result = s.threeSum(nums)
    print (result)


